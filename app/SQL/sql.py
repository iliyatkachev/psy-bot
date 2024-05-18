import asyncpg


connection = None



dsn = {
    'user': "postgres",
    'database': "psy_bot",
    'host': "127.0.0.1",
    'port': "5432"
}


async def fetch_administrator():
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            admin = await conn.fetch("SELECT id_admin, name FROM admin")
            return [{'id_admin': user['id_admin'], 'name': user['name']} for user in admin]


async def fetch_admin():
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            admin = await conn.fetch("SELECT id_admin FROM admin")
            return [user['id_admin'] for user in admin]


async def insert_admin(id_admin):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO admin (id_admin) VALUES ($1)", id_admin)


async def fetch_users():
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            users = await conn.fetch("SELECT user_id FROM users")
            return [user['user_id'] for user in users]


async def insert_users(user_id):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO users (user_id) VALUES ($1)", user_id)


async def add_admin():
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            admin = await conn.fetch("INSERT INTO id_admin FROM admin")
            return [user['id_admin'] for user in admin]


async def add_channel(name_channel, url, id_channel):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                'INSERT INTO channels (name_channel, url, id_channel) VALUES ($1, $2, $3)',
                name_channel, url, id_channel
            )


async def delete_all_channels(id_channel):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                'DELETE FROM channels WHERE id_channel = $1', id_channel
            )


async def delete_administrator(id_admin):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                'DELETE FROM admin WHERE id_admin = $1', id_admin
            )


async def fetch_urls_and_ids(id_channel):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                'INSERT INTO channels (id_channel) VALUES ($1)", id_channel', id_channel
            )


async def s_full_users():
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            full_users = await conn.execute(
                'SELECT user_id FROM users'
            )
            return full_users


async def add_administrator(name, id_admin):
    async with asyncpg.create_pool(**dsn) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                'INSERT INTO admin (name, id_admin) VALUES ($1, $2)', name, id_admin
            )
