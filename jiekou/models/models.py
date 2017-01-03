# # -*- coding: utf-8 -*-
# # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # Odoo Connector
# # QQ:61365857
# # 邮件:caobo@shmingjiang.org.cn
# # 手机：15562666538
# # 作者：'caobo'
# # 公司网址： www.goderp.com
# # 山东开源ERP有限公司
# # 日期：2015-12-18
# # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import logging
from openerp import fields,models,api
from datetime import datetime
date_ref = datetime.now().strftime('%Y-%m-%d')
_logger = logging.getLogger(__name__)

class stock_location_inherit(models.Model):
    _inherit = 'stock.location'
    # _description = "stock.location"

    location_code = fields.Char(string='门店编号', size=64, help="Location Code")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: