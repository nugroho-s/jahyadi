# jahyadi
bot jahyadi

## Setting up bot
### Postgres
First, you must initialize your database for the currency feature to work. You can use following create table query.
```
CREATE TABLE jahyadi.allowed_say (
    user_id bigint NOT NULL
);

CREATE TABLE jahyadi.users (
    user_id bigint NOT NULL,
    jahyadi_coin bigint DEFAULT 0,
    updated_time timestamp without time zone,
    last_steal timestamp without time zone,
    last_trivia timestamp without time zone
);
```
### Bot
Before you can run the bot, you must set these environments
```
BOT_TOKEN: Discord bot token from https://discord.com/developers/applications/
DATABASE_URL: Postgres database url in postgresql://<username>:<password>@<host>:<port>/<database> format
```
