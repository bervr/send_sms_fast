import configparser
import datetime
import os
import factory

from factory import alchemy


from send_database import ServerStorage
dir_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(f"{dir_path}/{'server.ini'}")
database = ServerStorage(
        os.path.join(
            # config['SETTINGS']['Database_path'],
            dir_path,
            config['SETTINGS']['Database_file']))

class UsersFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Users
        sqlalchemy_session = database.session  # the SQLAlchemy session object

    id = factory.Sequence(lambda n: n)
    number = factory.Faker('phone_number')
    prefix = factory.Faker('country_calling_code')
    tag = factory.Faker('paragraph', nb_sentences=1)

class CampainFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Campain
        sqlalchemy_session = database.session # the SQLAlchemy session object
    id = factory.Sequence(lambda n: n)
    start_time = factory.LazyFunction(datetime.datetime.now)
    stop_time = factory.LazyFunction(datetime.datetime.now)
    text = factory.Faker('paragraph', nb_sentences=5)
    filter = factory.Faker('paragraph', nb_sentences=1)

class MessagesFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Messages
        sqlalchemy_session = database.session  # the SQLAlchemy session object

    class Params:
        user = factory.SubFactory(UsersFactory)
        campain = factory.SubFactory(CampainFactory)
    user_id = factory.SelfAttribute('user.id')

    campain_id = factory.SelfAttribute('campain.id')
    status = factory.Faker('currency_code')


if __name__ == "__main__":

    for i in range(10):
        # MessagesFactory()
        database.session.add(MessagesFactory())
        database.session.commit()
