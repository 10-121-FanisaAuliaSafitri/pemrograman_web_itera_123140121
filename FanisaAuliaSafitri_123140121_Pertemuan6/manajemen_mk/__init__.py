from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import zope.sqlalchemy

def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        # Konfigurasi database engine berdasarkan file .ini
        engine = engine_from_config(settings, 'sqlalchemy.')
        session_factory = sessionmaker(bind=engine)
        
        # Fungsi untuk menyediakan dbsession pada setiap request
        def get_dbsession(request):
            session = session_factory()
            # Mendaftarkan session ke transaction manager agar commit otomatis
            zope.sqlalchemy.register(session, transaction_manager=request.tm)
            return session

        # Menyertakan dukungan manajemen transaksi (pyramid_tm)
        config.include('pyramid_tm')
        
        # Menggunakan add_request_method (pengganti add_request_property)
        config.add_request_method(get_dbsession, 'dbsession', reify=True)
        
        # Registrasi Routes sesuai instruksi tugas
        config.add_route('matakuliah_list', '/api/matakuliah')
        config.add_route('matakuliah_detail', '/api/matakuliah/{id}')
        
        config.scan()
    return config.make_wsgi_app()