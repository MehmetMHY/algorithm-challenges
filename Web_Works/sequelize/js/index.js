const sequelize = require("./connection")
const model = require("./model")

async function main() {
    await sequelize.sync()

    let entry = {
        "name": "example1",
        "subTable": [{
            "post": "post1"
        }]
    }

    await model.rootTable.create(entry, {
        include: [{
            model: model.subTable,
            as: "subTable",
            separate: true
        }]
    })

    let results = await model.rootTable.findAll({
        where: {},
        include: [{
            model: model.subTable,
            as: "subTable",
            separate: true
        }]
    })

    console.log(JSON.stringify(results, null, indent = 4))

    await sequelize.close()
}

// MAIN FUNCTION CALLS
main().then()