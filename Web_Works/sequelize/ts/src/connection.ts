import { Sequelize, Dialect} from "sequelize"

interface SequelizeConfig {
    username: string,
    password: string,
    database: string,
    host: string,
    dialect: Dialect,
    port: number,
    logging?: boolean
}

const config: SequelizeConfig = {
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

export default sequelize
