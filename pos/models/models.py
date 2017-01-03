# # # -*- coding: utf-8 -*-
# # # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # # Odoo Connector
# # # QQ:61365857
# # # 邮件:caobo@shmingjiang.org.cn
# # # 手机：15562666538
# # # 作者：'caobo'
# # # 公司网址： www.goderp.com
# # # 山东开源ERP有限公司
# # # 日期：2015-12-18
# # # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# import logging
# from openerp import fields,models,api
# from datetime import datetime
# date_ref = datetime.now().strftime('%Y-%m-%d')
# _logger = logging.getLogger(__name__)
#
# class caobo_template(models.Model):
#     _inherit = 'pos.order'
#     _description = "pos.order"
#
#     @api.multi
#     def create(self, values):
#         if values:
#             print '123'
#             # print values
#             value_objs = values["lines"]
#             print value_objs
#             for values_obj in value_objs:
#                 print values_obj[2]['qty'], values_obj[2]['product_id'], values['user_id']
#                 user_obj = self.pool('res.users').search([('id', '=', values['user_id'])])
#                 print user_obj
#                 print user_obj.id, user_obj.name
#                 print user_obj.partner_id
#                 location_obj = self.pool('stock.location').search([('partner_id', '=', user_obj.partner_id)])
#                 print location_obj
#                 query = "select sum(qty) as sum_qty from stock_quant where location_id = " + str(location_obj.id) + " and product_id=" + str(values_obj[2]['product_id'])
#                 self.cr.execute(query)
#                 info = self.cr.dictfetchall()
#                 print info[0]['sum_qty']
#                 print '**************'
#                 # raise UserError(u'不可以删除一个完成的单据')
#         else:
#             print '123'
#         return super(self).create(values)
#         # # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: