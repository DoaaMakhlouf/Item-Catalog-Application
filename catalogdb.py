import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

category1 = Category(name="Comedy")
session.add(category1)
session.commit()

item1 = Item(name="Forrest_Gump",
             description="""The presidencies of Kennedy and Johnson, Vietnam,
             Watergate, and other history unfold through the perspective of
             an Alabama man with an IQ of 75.""",
             category=category1)
session.add(item1)
session.commit()

item2 = Item(name="Modern_Times",
             description="""The Tramp struggles to live in modern industrial
             society with the help of a young homeless woman.""",
             category=category1)
session.add(item2)
session.commit()

item3 = Item(name="Amelie",
             description="""Amelie is an innocent and naive girl in Paris
             with her own sense of justice. She decides to help those around
             her and, along the way, discovers love.""",
             category=category1)
session.add(item3)
session.commit()

category2 = Category(name="Sci-Fi")
session.add(category2)
session.commit()

item4 = Item(name="Extinction",
             description="""A father has a recurring dream of losing his
             family. His nightmare turns into reality when the planet is
             invaded by a force bent on destruction. Fighting for their
             lives, he comes to realize an unknown strength to keep them safe
             from harm.""",
             category=category2)
session.add(item4)
session.commit()

item5 = Item(name="Venom",
             description="""When Eddie Brock acquires the powers of a
             symbiote, he will have to release his alter-ego 'Venom' to save
             his life.""",
             category=category2)
session.add(item5)
session.commit()

item6 = Item(name="Jurassic_World:Fallen_Kingdom",
             description="""When the island's dormant volcano begins roaring
             to life, Owen and Claire mount a campaign to rescue the
             remaining dinosaurs from this extinction-level event.""",
             category=category2)
session.add(item6)
session.commit()


category3 = Category(name="Horror")
session.add(category3)
session.commit()

item7 = Item(name="South_African_Spook_Hunter",
             description="""South African Spook Hunter Matty Vans hires a
             film crew to document his paranormal ghost hunting business.
             Just as they tire of following him around to find no evidence of
             the paranormal, he receives a phone call from a woman claiming
             her family is being hounded by a spirit. After agreeing to spend
             the week with the family, it quickly becomes clear to everyone
             but Matty Vans that their haunting is an elaborate hoax.
             However, the Damon-Murray family are also harbouring a dark
             secret.""",
             category=category3)
session.add(item7)
session.commit()

item8 = Item(name="The_Fear_Footage",
             description="""On April 19th, 2016, Deputy Leo Cole vanished.
             The next morning, his body camera was found.""",
             category=category3)
session.add(item8)
session.commit()

item9 = Item(name="Psychomanteum",
             description="""A portmanteau style feature length film made up
             of several very different short horror films shot in the UK.""",
             category=category3)
session.add(item9)
session.commit()


category4 = Category(name="Romance")
session.add(category4)
session.commit()

item10 = Item(name="Atonement",
              description="""Fledgling writer Briony Tallis, as a
              thirteen-year-old, irrevocably changes the course of several
              lives when she accuses her older sister's lover of a crime he
              did not commit.""",
              category=category4)
session.add(item10)
session.commit()

item11 = Item(name="The_Notebook",
              description="""A poor yet passionate young man falls in love
              with a rich young woman, giving her a sense of freedom, but they
              are soon separated because of their social differences.""",
              category=category4)
session.add(item11)
session.commit()

item12 = Item(name="Titanic",
              description="""A seventeen-year-old aristocrat falls in love
              with a kind but poor artist aboard the luxurious, ill-fated
              R.M.S. Titanic.""",
              category=category4)
session.add(item12)
session.commit()


category5 = Category(name="Action")
session.add(category5)
session.commit()

item13 = Item(name="The_Equalizer",
              description="""A man believes he has put his mysterious past
              behind him and has dedicated himself to beginning a new, quiet
              life. But when he meets a young girl under the control of
              ultra-violent Russian gangsters, he can't stand idly by - he has
              to help her.""",
              category=category5)
session.add(item13)
session.commit()

item14 = Item(name="Mad_Max:Fury_Road",
              description="""In a post-apocalyptic wasteland, a woman rebels
              against a tyrannical ruler in search for her homeland with the
              aid of a group of female prisoners, a psychotic worshiper, and a
              drifter named Max.""",
              category=category5)
session.add(item14)
session.commit()

item15 = Item(name="Logan",
              description="""In the near future, a weary Logan cares for an
              ailing Professor X, somewhere on the Mexican border. However,
              Logan's attempts to hide from the world, and his legacy, are
              upended when a young mutant arrives, pursued by dark forces.""",
              category=category5)
session.add(item15)
session.commit()
