import calendar

def create_calendar_page(month,year):

    page = ''
    days = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
    weekdays = calendar.Calendar()
    for i in weekdays.monthdayscalendar(year, month):
        for q in i:
            q = str(q)
            if q == 0:
                q = q.replace('0', ' ')
            if len(q) == 1:
                q = '0' + q
            page += q + ' '
        page = page + '\n'

    page = page.replace('00', '  ').replace(' \n', '\n')

    return days + page