# coding: utf-8

class credential:
    def __init__(self):
        # Fill out credentials
        self.userId = ""
        self.password = ""
        self.projectId = ""

    def get(self):
        return [self.userId, self.password, self.projectId]
