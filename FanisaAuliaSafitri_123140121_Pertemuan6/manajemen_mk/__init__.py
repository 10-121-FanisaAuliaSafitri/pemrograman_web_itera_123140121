from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import zope.sqlalchemy

def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        engine = engine_from_config(settings, 'sqlalchemy.')
        session_factory = sessionmaker(bind=engine)
        
        def get_dbsession(request):
            session = session_factory()
            zope.sqlalchemy.register(session, transaction_manager=request.tm)
            return session

        config.include('pyramid_tm')
        
        config.add_request_method(get_dbsession, 'dbsession', reify=True)

        config.add_route('matakuliah_list', '/api/matakuliah')
        config.add_route('matakuliah_detail', '/api/matakuliah/{id}')
        
        config.scan()

    return config.make_wsgi_app()
