from pyramid.view import view_config
from pyramid.response import Response
from .models import Matakuliah

@view_config(route_name='matakuliah_list', renderer='json', request_method='GET')
def get_all_matakuliah(request):
    query = request.dbsession.query(Matakuliah).all()
    return {'matakuliahs': [mk.to_dict() for mk in query]}

@view_config(route_name='matakuliah_list', renderer='json', request_method='POST')
def create_matakuliah(request):
    try:
        data = request.json_body
        new_mk = Matakuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=int(data['sks']),
            semester=int(data['semester'])
        )
        request.dbsession.add(new_mk)
        # Flush untuk mendapatkan ID jika diperlukan
        request.dbsession.flush() 
        return {'status': 'success', 'data': new_mk.to_dict()}
    except Exception as e:
        print(f"Error detail: {e}")
        # Gunakan response sederhana untuk error
        request.response.status = 500
        return {'error': str(e)}