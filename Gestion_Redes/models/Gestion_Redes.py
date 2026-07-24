# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Gestion_Redes(models.Model):
    _name = 'gestion.redes'
    _description = 'Gestion de Redes'

    Nombre_del_dispositivo = fields.Char(string='Nombre del Dispositivo', required=True)
    Modelo = fields.Char(string='Modelo', required=True)
    Marca = fields.Char(string='Marca', required=True)
    
    # Campo para la Imagen del Dispositivo
    imagen = fields.Binary(string='Imagen del Dispositivo', attachment=True)
    
    # Selector por medio de una lista (Tipo de dispositivo)
    tipo_dispositivo = fields.Selection([
        ('router', 'Router'),
        ('switch', 'Switch'),
        ('access_point', 'Access Point'),
        ('firewall', 'Firewall'),
        ('servidor', 'Servidor de Red'),
        ('otro', 'Otro')
    ], string='Tipo de Dispositivo', default='router', required=True)

    # Selector de Estado para la gráfica y Kanban
    estado_dispositivo = fields.Selection([
        ('disponible', 'Disponible'),
        ('en_mantenimiento', 'En Mantenimiento'),
        ('baja', 'Dado de Baja')
    ], string='Estado del Dispositivo', default='disponible', required=True)

    Fecha_de_Mantenimiento = fields.Datetime(string='Fecha de Mantenimiento', required=True)
    Fecha_de_Alta_Dispositivo = fields.Datetime(string='Fecha de Alta Dispositivo', required=True)
    Numero_Serie = fields.Char(string='Número de Serie', required=True)
    DNS = fields.Char(string='DNS', required=True)
    Sistema_Firmware = fields.Char(string='Sistema / Firmware', required=True)
