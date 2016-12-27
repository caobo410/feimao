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

class supplier_info(models.Model):
    _name = "supplier.info"
    _description = "supplier.info"

    code = fields.Char(string='编号', size=64, required=True, help="编号")
    name = fields.Char(string='名称', size=64, required=True, help="名称")
    zj_code = fields.Char(string='助记码', size=64, help="助记码")
    type = fields.Selection([('1', '直送'),('2','提货')], '配送类型', required=True, help="配送类型")
    address = fields.Char(string='通讯地址', size=64, help="助记码")
    post_code = fields.Char(string='邮编', size=64, help="邮编")
    company_type = fields.Char(string='企业类型', size=64, help="企业类型")
    bank = fields.Char(string='开户行', help="开户行")
    bank_account = fields.Char(string='银行账户', size=64, help="银行账户")
    payment = fields.Char(string='结算方式', size=64, help="结算方式")
    legal_person = fields.Char(string='法人代表', size=64, help="法人代表")
    tel = fields.Char(string='联系电话', size=64, help="联系电话")
    phone = fields.Char(string='手机', size=64, help="手机")
    supplier_id = fields.One2many('supplier.line', 'supplier_id', string='明细',copy=True)
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='Date', size=64, required=True, help="创建日期")

    _defaults = {
        'type': '1',
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
class supplier_line(models.Model):
    _name = "supplier.line"
    _description = "supplier.line"

    name = fields.Char(string='姓名', size=64, required=True, help='姓名')
    tel = fields.Char(string='电话', help="电话")
    supplier_id = fields.Many2one('supplier.info', string='关联', select=True, track_visibility='onchange')
    phone_one = fields.Char(string='手机1', help="手机1")
    phone_two = fields.Char(string='手机2', help="手机2")
    address = fields.Char(string='家庭地址', help="家庭地址")
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='Date', size=64, required=True, help="创建日期")

    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: