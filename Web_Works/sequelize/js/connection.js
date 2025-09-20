const {
    Sequelize
} = require("sequelize")

const config = {
    "username": "postgres",
    "password": "password",
    "database": "postgres",
    "host": "localhost",
    "dialect": "postgres",
    "port": 5432
}

const sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.host,
    dialect: config.dialect,
    port: config.port,
    logging: false
})

module.exports = sequelize