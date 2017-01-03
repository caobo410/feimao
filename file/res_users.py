import math

from openerp.osv import osv, fields

import openerp.addons.product.product


class res_users(osv.osv):
    _inherit = 'res.users'
    _columns = {
        'ean13': fields.char('EAN13', size=13, help="BarCode"),
        'pos_config': fields.many2one('pos.config', 'Default Point of Sale', domain=[('state', '=', 'active')]),
    }

    def _check_ean(self, cr, uid, ids, context=None):
        return all(
            openerp.addons.product.product.check_ean(user.ean13) == True
            for user in self.browse(cr, uid, ids, context=context)
        )

    def _check_pos_config(self, cr, uid, ids, context=None):
        current = self.browse(cr, uid, ids, context=context)
        users = self.search(cr, uid, [], context=context)
        for id in users:
            if id == current.id:
                continue
            user = self.browse(cr, uid, id, context=context)
            if user.pos_config == current.pos_config:
                return False
        return True

    _constraints = [
        (_check_pos_config, u"Error: Pos confing not allow complete", ['pos_config'],),
        (_check_ean, "Error: Invalid ean code", ['ean13'],),
    ]
