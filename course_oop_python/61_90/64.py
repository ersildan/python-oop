class Config:
    _instance = None

    program_name = 'GenerationPy'
    environment = 'release'
    loglevel = 'verbose'
    version = '1.0.0'

    def __new__(cls, *args, **kwargs):
        # conf = super().__new__(cls) каждый раз новый объект
        # return conf

        if cls._instance is None: # Если еще нет объекта
            cls._instance = super().__new__(cls) # создаем один раз

        return cls._instance  # возвращает сохраненный объект


config1 = Config()
config2 = Config()

print(config1 is config2)
print(config1.program_name) # GenerationPy
