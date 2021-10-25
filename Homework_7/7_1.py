# task №7_1 by Kirill Peregud

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, ForeignKey, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('sqlite:///university.db', echo=True)
conn = engine.connect()
meta = MetaData()

speciality = Table(
    'speciality', meta,
    Column('id', Integer, primary_key=True),
    Column('title_spec', String),
)

student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('last_name', String),
    Column('speciality_id', Integer, ForeignKey('speciality.id')),
)


subject = Table(
    'subject', meta,
    Column('id', Integer, primary_key=True),
    Column('title_subj', String),
)


speciality_2_subject = Table(
    'speciality_2_subject', meta,
    Column('subject_id', Integer, ForeignKey('subject.id')),
    Column('speciality_id', Integer, ForeignKey('speciality.id')),
)


faculty = Table(
    'faculty', meta,
    Column('id', Integer, primary_key=True),
    Column('title_fac', String),
)


faculty_2_speciality = Table(
    'faculty_2_speciality', meta,
    Column('id_faculity', Integer, ForeignKey('faculty.id')),
    Column('speciality_id', Integer, ForeignKey('speciality.id')),
)


university = Table(
    'university', meta,
    Column('id', Integer, primary_key=True),
    Column('title_univ', String),
)


university_2_faculty = Table(
    'university_2_faculty', meta,
    Column('id_university', Integer, ForeignKey('university.id')),
    Column('id_faculity', Integer, ForeignKey('faculty.id')),
)


# conn.execute(
#     student.insert(),
#     [
#         {'name': 'Oleg', 'last_name': 'Herbet', 'speciality_id': 1},
#         {'name': 'Ivan', 'last_name': 'Solovey', 'speciality_id': 1},
#         {'name': 'Maria', 'last_name': 'Otarova', 'speciality_id': 2},
#     ]
# )


# conn.execute(
#     subject.insert(),
#     [
#         {'title_subj': 'Maths'},
#         {'title_subj': 'History'},
#         {'title_subj': 'Theoretical mechanics'},
#     ]
# )


# conn.execute(
#     speciality.insert(),
#     [
#         {'title_spec': 'Industrial robots'},
#         {'title_spec': 'Information Systems'},
#         {'title_spec': 'Economy'},
#     ]
# )


# conn.execute(
#     speciality_2_subject.insert(),
#     [
#         {'subject_id': 1, 'speciality_id': 1},
#         {'subject_id': 1, 'speciality_id': 2},
#         {'subject_id': 1, 'speciality_id': 3},
#         {'subject_id': 2, 'speciality_id': 2},
#         {'subject_id': 3, 'speciality_id': 2},
#         {'subject_id': 3, 'speciality_id': 1},
#     ]
# )


# conn.execute(
#     faculty.insert(),
#     [
#         {'title_fac': 'FITR'},
#         {'title_fac': 'Faculty of Energy'},
#         {'title_fac': 'Automotive faculty'},
#     ]
# )


# conn.execute(
#     faculty_2_speciality.insert(),
#     [
#         {'id_faculity': 1, 'speciality_id': 1},
#         {'id_faculity': 1, 'speciality_id': 2},
#         {'id_faculity': 2, 'speciality_id': 3},
#         {'id_faculity': 3, 'speciality_id': 3},
#     ]
# )


# conn.execute(
#     university.insert(),
#     [
#         {'title_univ': 'BNTU'},
#         {'title_univ': 'BGUIR'},
#         {'title_univ': 'BGU'},
#     ]
# )


# conn.execute(
#     university_2_faculty.insert(),
#     [
#         {'id_university': 1, 'id_faculity': 1},
#         {'id_university': 1, 'id_faculity': 3},
#         {'id_university': 2, 'id_faculity': 2},
#         {'id_university': 3, 'id_faculity': 1},
#     ]
# )


j = student.join(speciality, student.c.speciality_id == speciality.c.id)
all_students = select([speciality, student]).select_from(j).where(student.c.speciality_id == 1)

result = conn.execute(all_students)
print([row[1:5] for row in result])

meta.create_all(engine)