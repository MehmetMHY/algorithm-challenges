import { Sequelize, Model, Op, DataTypes } from "sequelize";
import sequelize from "./connection.js";
import { rootTable, subTable } from "./model.js";

async function main() {
  await sequelize.sync();

  let entry = {
    name: "example1",
    subTable: [
      {
        post: "post1",
      },
    ],
  };

  await rootTable.create(entry, {
    include: [
      {
        model: subTable,
        as: "subTable",
        separate: true,
      },
    ],
  });

  let results = await rootTable.findAll({
    where: {},
    include: [
      {
        model: subTable,
        as: "subTable",
        separate: true,
      },
    ],
  });

  console.log(JSON.stringify(results, null, 2));

  await sequelize.close();
}

// MAIN FUNCTION CALLS
main().then();
