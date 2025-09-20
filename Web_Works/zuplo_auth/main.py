from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from hashlib import sha256
import secrets
import uuid
from datetime import datetime

app = Flask(__name__)
Base = declarative_base()


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    user_id = Column(String, nullable=False)  # Assuming UUID string format
    hash = Column(String, unique=True, nullable=False)
    expiration_date = Column(DateTime)


engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def hash_key(key):
    return sha256(key.encode()).hexdigest()


def create_checksum(api_key):
    total = 0
    add_it = True
    for c in api_key:
        if c.isdigit():
            num_val = int(c)
            if add_it:
                total += num_val
                add_it = False
            else:
                total -= num_val
                add_it = True
    value = str(abs(total)).zfill(4)[:4]
    first_char = api_key[0]
    last_char = api_key.replace("-", "")[-1]
    return f"{first_char}{last_char}{value}"


def generate_key():
    api_key = f"{uuid.uuid4()}-{secrets.token_hex(16)}"
    checksum = create_checksum(api_key)
    key = f"{api_key}-{checksum}"
    hashed_key = hash_key(key)
    return {"key": key, "hash": hashed_key}


def initial_key_verification(api_key):
    if len(api_key) != 76:
        return False
    dash_positions = [8, 13, 18, 23, 36, 69]
    if any(api_key[pos] != "-" for pos in dash_positions):
        return False
    expected_checksum = create_checksum(api_key[:70])
    print(api_key, expected_checksum)
    actual_checksum = api_key[70:]
    print("===>", expected_checksum, actual_checksum)
    return expected_checksum == actual_checksum


###################################################################################################


@app.route("/validate_api_key", methods=["POST"])
def validate_api_key():
    api_key = request.headers.get("Authorization", "Bearer ")[7:]
    if not initial_key_verification(api_key):
        return jsonify({"code": 401, "msg": "Invalid API key V2", "status": False})

    api_key_hash = hash_key(api_key)
    session = Session()
    entry = session.query(APIKey).filter_by(hash=api_key_hash).one_or_none()

    if entry and entry.expiration_date > datetime.now():
        return jsonify({"code": 200, "msg": "API key is valid", "status": True})
    else:
        return jsonify({"code": 401, "msg": "Invalid API key", "status": False})


@app.route("/add_api_key", methods=["POST"])
def add_api_key():
    try:
        data = request.json
        new_key = generate_key()
        new_api_key = APIKey(
            name=data["name"],
            user_id=data["user_id"],
            hash=new_key["hash"],
            expiration_date=datetime.strptime(str(data["expiration_date"]), "%Y-%m-%d"),
        )
        session = Session()
        session.add(new_api_key)
        session.commit()
        return jsonify(
            {
                "code": 200,
                "msg": "API key added successfully",
                "key": new_key["key"],
                "status": True,
            }
        )
    except Exception as e:
        return jsonify({"code": 500, "msg": str(e), "status": False})


@app.route("/delete_api_key", methods=["DELETE"])
def delete_api_key():
    try:
        api_key_id = request.args.get("id")
        print(api_key_id)
        session = Session()
        entry = session.query(APIKey).filter_by(id=api_key_id).one_or_none()
        if entry:
            session.delete(entry)
            session.commit()
            return jsonify(
                {"code": 200, "msg": "API key deleted successfully", "status": True}
            )
        else:
            return jsonify({"code": 404, "msg": "API key not found", "status": False})
    except Exception as e:
        session.rollback()  # Rollback in case of any error
        return jsonify({"code": 500, "msg": str(e), "status": False})
    finally:
        session.close()  # Ensure session is closed after the operation


@app.route("/get_all_api_keys", methods=["GET"])
def get_all_api_keys():
    session = Session()
    try:
        api_keys = session.query(APIKey).all()
        keys_list = [
            {
                "id": key.id,
                "name": key.name,
                "user_id": key.user_id,
                "hash": key.hash,
                "expiration_date": (
                    key.expiration_date.isoformat() if key.expiration_date else None
                ),
            }
            for key in api_keys
        ]
        return jsonify(keys_list), 200
    except Exception as e:
        session.rollback()
        return jsonify({"msg": str(e), "status": False}), 500
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)
