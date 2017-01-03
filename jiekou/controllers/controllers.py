# # -*- coding: utf-8 -*-
# from openerp import http
# from openerp import http, fields
# import authorizer
# import rest
# from datetime import datetime
#
# try:
#     import cStringIO as StringIO
# except ImportError:
#     import StringIO
#
#
# date_ref = datetime.now().strftime('%Y-%m-%d')
# # _logger = logging.getLogger(__name__)
#
# class OrderController(http.Controller):
#     #获取商品编码
#     @authorizer.authorize
#     @http.route('/api/goods/get_goods_code/<database>', type='http', auth='none', methods=['GET'])
#     def get_goods_code(self, database, login, password, goodcode):
#         product_objs = self.current_env['product_product'].search([('ean13', '=', goodcode)])
#         if not product_objs:
#             return rest.render_json({"status": "no", "message": "商品编码不存在", "data": ''})
#         defaults_code = ''
#         for batch_obj in product_objs:
#             defaults_code = batch_obj.defaults_code + ';'
#         return rest.render_json({"status": "yes", "message": defaults_code, "data": defaults_code})
#
#     #获取单品库存
#     @authorizer.authorize
#     @http.route('/api/goods/get_goods_dpkc/<database>', type='http', auth='none', methods=['GET'])
#     def get_goods_dpkc(self, database, login, password, goods_list):
#         print goods_list
#         goods_values = eval(goods_list)
#         print goods_values
#         print goods_values['huojia']
#         print goods_values['sid']
#         goods_obj = self.current_env['product.product'].search([('default', '=', goods_values['huojia'])])
#         if not goods_obj:
#             return rest.render_jzson({"status": "no", "message": '商品不存在', "data": 'false'})
#         location_obj = self.current_env['stock.location'].search([('location_code', '=', goods_values['sid'])])
#         if not location_obj:
#             return rest.render_jzson({"status": "no", "message": '门店编号不存在', "data": 'false'})
#         quant_objs = self.current_env['stock.quant'].search([('location_id', '=', location_obj.id), ('product_id', '=', goods_obj.id)])
#         quant_num = 0
#         if not quant_objs:
#             return rest.render_jzson({"status": "no", "message": '库存为0', "data": 'false'})
#         for quant_obj in quant_objs:
#             quant_num = quant_obj.qty
#         if quant_num < int(goods_values['num']):
#             return rest.render_jzson({"status": "yes", "message": '大于ERP库存', "data": 'false'})
#         return rest.render_jzson({"status": "yes", "message": '库存为' + str(quant_num), "data": 'true'})
#
#     # @authorizer.authorize
#     # @http.route('/api/goods/get_xsch_code/<database>', type='http', auth='none', methods=['GET'])
#     # def get_goods_code(self, database, login, password, goods_list):
#     #     goods_values = eval(goods_list)
#     #     goods_obj = self.current_env['product.product'].search([('default', '=', goods_values['huojia'])])
#     #     if not goods_obj:
#     #         return rest.render_jzson({"status": "no", "message": '商品不存在', "data": 'false'})
#     #     location_obj = self.current_env['stock.location'].search([('location_code', '=', goods_values['sid'])])
#     #     if not location_obj:
#     #         return rest.render_jzson({"status": "no", "message": '门店编号不存在', "data": 'false'})
#     #     quant_objs = self.current_env['stock.quant'].search([('location_id', '=', location_obj.id), ('product_id', '=', goods_obj.id)])
#     #     quant_num = 0
#     #     if not quant_objs:
#     #         return rest.render_jzson({"status": "no", "message": '库存为0', "data": 'false'})
#     #     for quant_obj in quant_objs:
#     #         quant_num = quant_obj.qty
#     #     if quant_num < int(goods_values['num']):
#     #         return rest.render_jzson({"status": "yes", "message": '大于ERP库存', "data": 'false'})
#     #     return rest.render_jzson({"status": "yes", "message": '库存为' + str(quant_num), "data": 'true'})