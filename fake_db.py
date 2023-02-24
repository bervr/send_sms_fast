from datetime import timedelta

from factory import alchemy, Sequence, RelatedFactory, Faker
from faker import factory

from send_database import ServerStorage


class UsersFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Users
        sqlalchemy_session = ServerStorage.session  # the SQLAlchemy session object

    number = [Faker().unique.phone_number() for i in range(500)]
    prefix = Faker().country_calling_code()
    tag = Faker().paragraph(nb_sentences=1)

class CampainFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Campain
        sqlalchemy_session = ServerStorage.session # the SQLAlchemy session object

    start_time = Faker().date_time()
    stop_time = start_time + timedelta('5h')
    text = Faker().paragraph(nb_sentences=5)
    filter = Faker().paragraph(nb_sentences=1)

class MessagesFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ServerStorage.Messages
        sqlalchemy_session = ServerStorage.session # the SQLAlchemy session object

    user_id = factory.SubFactory(UsersFactory)
    campain_id = factory.SubFactory(CampainFactory)
    send_time = Faker().date_time()
    status = Faker().currency_code()


if __name__ == "__main__":

    for i in range(10):
        MessagesFactory()
        ServerStorage.session.add(MessagesFactory())
        ServerStorage.session.session.commit()
    # group_from_factory = GroupFactory(name='a new group name')
    # assert group_from_factory.group_pk is None
    # # Save it to our DB
    # db.session.add(group_from_factory)
    # db.session.commit()