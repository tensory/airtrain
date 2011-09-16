import web
import checker
import view
from view import render

urls = (
    '/toys/airtrain', 'index'
)

class index:
    def GET(self):
        sources = checker.get_info()
        return render.base(view.status(sources))
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
