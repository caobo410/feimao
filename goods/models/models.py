# -*- coding: utf-8 -*-
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Odoo Connector
# QQ:61365857
# 邮件:caobo@shmingjiang.org.cn
# 手机：15562666538
# 作者：'caobo'
# 公司网址： www.goderp.com
# 山东开源ERP有限公司
# 日期：2015-12-18
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import logging
from openerp import fields,models,api
from datetime import datetime
date_ref = datetime.now().strftime('%Y-%m-%d')
_logger = logging.getLogger(__name__)

class brand_info(models.Model):
    _name = 'brand.info'
    _description = 'brand.info'

    code = fields.Char(string='品牌编号', size=64, required=True, help='品牌编号')
    name = fields.Char(string='品牌名称', size=64, required=True, help='品牌名称')
    messages = fields.Char(string='备注', help='备注')
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='日期', size=64, required=True, help='单据日期')

    @api.multi
    def name_get(self):
        res = []
        for brand in self:
            res.append((brand.id, brand.code and (brand.code + '_' + brand.name) or brand.name))
        return res

    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
class classification_info(models.Model):
    _name = 'classification.info'
    _description = 'classification.info'

    code = fields.Char(string='分类编号', size=64, required=True, help='分类编号')
    name = fields.Char(string='分类名称', size=64, required=True, help='分类名称')
    messages = fields.Char(string='备注', help='备注')
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='日期', size=64, required=True, help='单据日期')

    @api.multi
    def name_get(self):
        res = []
        for classification in self:
            res.append((classification.id, classification.code and (classification.code + '_' + classification.name) or classification.name))
        return res
    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
class unit_info(models.Model):
    _name = 'unit.info'
    _description = 'unit.info'

    code = fields.Char(string='单位编号', size=64, required=True, help='单位编号')
    name = fields.Char(string='单位名称', size=64, required=True, help='单位名称')
    messages = fields.Char(string='备注', help='备注')
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='Date', size=64, required=True, help='单据日期')

    @api.multi
    def name_get(self):
        res = []
        for unit_info in self:
            res.append((unit_info.id, unit_info.code and (unit_info.code + '_' + unit_info.name) or unit_info.name))
        return res
    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
class goods_info(models.Model):
    _name = 'goods.info'
    _description = 'goods.info'

    code = fields.Char(string='商品编号', size=64, required=True, help='商品编号')
    name = fields.Char(string='商品名称', size=64, required=True, help='商品名称')
    zj_code = fields.Char(string='助记码', size=64, help='助记码')
    bar_code = fields.Char(string='条形码', help='条形码')
    one_classification_id = fields.Many2one('classification.info', string='一级分类', select=True, track_visibility='onchange')
    two_classification_id = fields.Many2one('classification.info', string='二级分类', select=True, track_visibility='onchange')
    brand_id = fields.Many2one('brand.info', string='品牌', select=True, track_visibility='onchange')
    unit_id = fields.Many2one('unit.info', string='单位', select=True, track_visibility='onchange')
    fz_unit_id = fields.Many2one('unit.info', string='辅助单位', select=True, track_visibility='onchange')
    discount = fields.Float(string='转换率(单位与辅助单位转换)', default=0.0)
    jy_price = fields.Float(string='建议进价', help='建议进价', default=0.0)
    jyls_price = fields.Float(string='建议零售价', help='建议零售价', default=0.0)
    image = fields.Binary(string='图片', help='图片')
    messages = fields.Char(string='备注', help='备注')
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='Date', size=64, required=True, help='单据日期')

    @api.multi
    def name_get(self):
        res = []
        for goods in self:
            res.append((goods.id, goods.code and (goods.code + '_' + goods.name) or goods.name))
        return res
    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: