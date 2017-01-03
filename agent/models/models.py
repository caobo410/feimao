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

class fm_agent(models.Model):
    _name = 'fm.agent'
    _description = 'fm.agent'

    code = fields.Char(string='代理编号', size=64, required=True, help='代理编号')
    name = fields.Char(string='代理名称', size=64, required=True, help='代理名称')
    persons_responsible = fields.Char(string='负责人', help='负责人')
    tel = fields.Char(string='电话', help='电话')
    address = fields.Char(string='地址', help='地址')
    operator = fields.Many2one('res.users', string='登录用户')
    join_date = fields.Date(string='加盟日期', size=64, help='加盟日期')
    line_id = fields.One2many('agent.line', 'line_id', string='明细', copy=True)
    messages = fields.Char(string='备注', help='备注')
    user_id = fields.Many2one('res.users', string='操作人')
    date_confirm = fields.Date(string='单据日期', size=64, required=True, help='单据日期')

    @api.multi
    def name_get(self):
        res = []
        for fm_agent in self:
            res.append((fm_agent.id, fm_agent.code and (fm_agent.code + '_' + fm_agent.name) or fm_agent.name))
        return res

    _defaults = {
        'join_date': date_ref,
        'date_confirm': date_ref,
        'user_id': lambda cr, uid, id, c={}: id,
    }

class agent_line(models.Model):
    _name = 'agent.line'
    _description = 'agent.line'

    line_id = fields.Many2one('fm.agent', string='关联')
    name = fields.Many2one('fm.store', string='门店', select=True, track_visibility='onchange')
    persons_responsible = fields.Char(string='负责人', help='负责人')
    tel = fields.Char(string='电话', help='电话')
    address = fields.Char(string='地址', help='地址')

    @api.one
    @api.onchange('name')
    def onchange_name(self):
        self.persons_responsible = self.name.persons_responsible
        self.tel = self.name.tel
        self.address = self.name.address
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: