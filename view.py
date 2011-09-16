import web
import config

t_globals = dict(
    datestr=web.datestr
)
render = web.template.render('templates/', cache=config.cache, 
                             globals=t_globals)
render._keywords['globals']['render'] = render

""" Only has one rendering method, to render the status page. """
def status(content):
    return render.status(content)
