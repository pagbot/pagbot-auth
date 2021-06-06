

class CreateAuth:

    def __init__(self, repository):
        self.auth_repository = repository

    async def create(self):
        return await self.auth_repository.create()
