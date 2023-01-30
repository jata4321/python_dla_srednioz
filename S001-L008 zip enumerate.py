projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, leader in zip(projects, leaders):
    print(f'The leader of {project} is {leader}')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, date, leader in list(zip(projects, dates, leaders)):
    print(f'The leader of project {project}, started {date} is {leader}')

for enum, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print(f'{enum} - The leader of project {project}, started {date} is {leader}')

project_list = list(zip(projects, dates, leaders))

for i, j, k in project_list:
    print(j, i, k)
