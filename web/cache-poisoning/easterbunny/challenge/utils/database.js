const sqlite3 = require("sqlite3");

class Database {
  constructor(db_file) {
    this.db_file = db_file;
    this.db = undefined;
  }

  async connect() {
    this.db = new sqlite3.Database(this.db_file);
  }

  async migrate() {
    return new Promise((resolve, reject) => {
      this.db.exec(
        `
            DROP TABLE IF EXISTS messages;

            CREATE TABLE IF NOT EXISTS messages (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                message   VARCHAR(300) NOT NULL,
                hidden    INTEGER NOT NULL
            );

            INSERT INTO messages (id, message, hidden) VALUES
              (1, "Dear Easter Bunny,\nPlease could I have the biggest easter egg you have?\n\nThank you\nGeorge", 0),
              (2, "Dear Easter Bunny,\nCould I have 3 chocolate bars and 2 easter eggs please!\nYours sincerely, Katie", 0),
              (3, "Dear Easter Bunny, Santa's better than you! HTB{f4k3_fl4g_f0r_t3st1ng}", 1),
              (4, "Hello Easter Bunny,\n\nCan I have a PlayStation 5 and a chocolate chick??", 0),
              (5, "Dear Easter Bunny,\nOne chocolate and marshmallow bunny please\n\nLove from Milly", 0),
              (6, "Dear Easter Bunny,\n\nHow are you? I'm fine please may I have 31 chocolate bunnies\n\nThank you\nBeth", 0);
            `,
        (error) => {
          if (error) {
            reject(error);
          } else {
            resolve();
          }
        },
      );
    });
  }

  async getMessage(id) {
    return new Promise((resolve, reject) => {
      this.db.get("SELECT * FROM messages WHERE id = ?", [id], (error, row) => {
        if (error) {
          reject(error);
        } else {
          resolve(row);
        }
      });
    });
  }

  async getMessageCount() {
    return new Promise((resolve, reject) => {
      this.db.get("SELECT COUNT(*) as count FROM messages", (error, row) => {
        if (error) {
          reject(error);
        } else {
          resolve(row.count);
        }
      });
    });
  }

  async insertMessage(message) {
    return new Promise((resolve, reject) => {
      this.db.run(
        "INSERT INTO messages (message, hidden) VALUES (?, ?)",
        [message, 0],
        function (error) {
          if (error) {
            reject(error);
          } else {
            resolve({ lastID: this.lastID });
          }
        },
      );
    });
  }
}

module.exports = Database;
