const { Sequelize, Model, Op, DataTypes } = require("sequelize");
const sequelize = require("./connection");

const schemaName = "public";

class rootTable extends Model {}
rootTable.init(
  {
    id: {
      type: DataTypes.UUID,
      primaryKey: true,
      defaultValue: Sequelize.UUIDV4,
    },
    name: {
      type: DataTypes.STRING,
    },
  },
  {
    sequelize,
    modelName: "rootTable",
    schema: schemaName,
    timestamps: true,
  },
);

class subTable extends Model {}
subTable.init(
  {
    id: {
      type: DataTypes.UUID,
      primaryKey: true,
      defaultValue: Sequelize.UUIDV4,
    },
    post: {
      type: DataTypes.STRING,
    },
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
subTable.belongsTo(rootTable, {
  foreignKey: "rootTableId",
});

module.exports = {
  rootTable,
  subTable,
};
