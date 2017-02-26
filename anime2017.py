# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

######################################################################

from openerp.osv import fields, osv , orm
from datetime import time, datetime
from openerp.tools.translate import _


class anime2017_modelo(osv.osv):
	_name = 'anime2017.modelo'
	_description = 'Formulario de Anime'
	_columns = {
	    # Campo oblidatorio para buscar , readonly = True
		'portada' : fields.binary('Portada'),
        'name' : fields.char('Nombre' , size=256, required=True, help='Nombre del anime'),
		'nom_orig' : fields.char('Nombre original', size=256),
		'tipo' : fields.char('Tipo', size=256),
		'capitulos' : fields.integer('Episodios' ,required=True),
		'estado' : fields.char('Estado', size=256),
		'fecha_ini' : fields.date('Fecha de inicio'),
		'fecha_end' :fields.date('Fecha de conclusion'),
		'season' : fields.char('Temporada', size=256),
		'autor' : fields.char('Autor', size=256),
		'estudio' : fields.char('Estudio' , size=256, required=True),
        'genero' : fields.char('Genero' , size=256, required=True),
		'fuente' : fields.char('Fuente', size=256),
		'nota' : fields.char('Nota', size=10),
		'duracion' : fields.char('Duracion', size=100),
		'calificacion' : fields.char('Calificacion', size=100),

		#autor, fecha de inicio y fecha de finalizacion, adaptacion u original
		#nota que tiene en mal, secuela o precuela, tipo, nombre original, duracion, fuente
	}
	_defaults = {
       'active' : 'true',
	}
anime2017_modelo()
