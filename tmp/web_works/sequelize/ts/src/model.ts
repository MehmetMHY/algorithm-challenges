import { Sequelize, Model, Op, DataTypes } from "sequelize";
import sequelize from "./connection.js";

const schemaName = "public";

interface rootTableAttributes {
  id: number;
  name: string;
}

class rootTable extends Model<rootTableAttributes, rootTableAttributes> {
  public id: number;
  public name: string;
}

rootTable.init(
  {
    id: {
      type: DataTypes.UUID,
      primaryKey: true,
      defaultValue: DataTypes.UUIDV4,
    },
    name: { type: DataTypes.STRING },
  },
  {
    sequelize: sequelize,
    modelName: "rootTable",
    schema: schemaName,
    timestamps: true,
  },
);

interface subTableAttributes {
  id: number;
  post: string;
  rootTableId: number;
}

class subTable extends Model<subTableAttributes, subTableAttributes> {
  public id: number;
  public post: string;
  public rootTableId: number;
}

subTable.init(
  {
    id: {
      type: DataTypes.UUID,
      primaryKey: true,
      defaultValue: DataTypes.UUIDV4,
    },
    post: { type: DataTypes.STRING },
    rootTableId: {
      type: DataTypes.UUID,
      field: "rootTableId",
      references: {
        model: rootTable,
        key: "id",
      },
    },
  },
  {
    sequelize,
    modelName: "subTable",
    schema: schemaName,
    timestamps: true,
  },
);

rootTable.hasMany(subTable, {
  foreignKey: "rootTableId",
  as: "subTable",
  onDelete: "CASCADE",
});
subTable.belongsTo(rootTable, { foreignKey: "rootTableId" });

export { rootTable };
export { subTable };
