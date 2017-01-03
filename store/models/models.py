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
from openerp import fields, models, api
from datetime import datetime
date_ref = datetime.now().strftime('%Y-%m-%d')
_logger = logging.getLogger(__name__)

class fm_store(models.Model):
    _name = "fm.store"
    _description = "fm.store"

    code = fields.Char(string='门店编号', size=64, required=True, help="门店编号")
    name = fields.Char(string='门店名称', size=64, required=True, help="门店名称")
    persons_responsible = fields.Char(string='负责人', help="负责人")
    tel = fields.Char(string='电话', help="电话")
    address = fields.Char(string='地址', help="地址")
    operator = fields.Many2one('res.users', string='登录用户')
    open_date = fields.Date(string='开业日期', size=64, required=True, help="开业日期")
    line_id = fields.Many2one('fm.agent', string='代理', select=True, track_visibility='onchange')
    messages = fields.Char(string='备注', help="备注")
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='单据日期', size=64, required=True, help="单据日期")

    @api.multi
    def name_get(self):
        res = []
        for fm_store in self:
            res.append((fm_store.id, fm_store.code and (fm_store.code + '_' + fm_store.name) or fm_store.name))
        return res

    _defaults = {
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: