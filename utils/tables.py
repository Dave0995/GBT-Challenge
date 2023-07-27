import sqlalchemy as sa

metadata = sa.MetaData()

hired_employees = sa.Table(
    'test_hired_employees',
    metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('name', sa.String(30)),
    sa.Column('datetime', sa.String(20)),
    sa.Column('department_id', sa.ForeignKey('test_departments.id')),
    sa.Column('job_id', sa.ForeignKey('test_jobs.id')),
    sa.Index('idx_datetime', 'datetime')
)

departments = sa.Table(
    'test_departments',
    metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('department', sa.String(20)),
    sa.Index('idx_department', 'department')
)

jobs = sa.Table(
    'test_jobs',
    metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('job', sa.String(20)),
    sa.Index('idx_job', 'job')
)
