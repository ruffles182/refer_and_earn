# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################
from . import models
from . import controllers
from logging import getLogger
_logger = getLogger(__name__)

def pre_init_check(self):
    from odoo.service import common
    from odoo.exceptions import Warning
    data_version = common.exp_version()
    version_info =  data_version.get('server_serie')
    if version_info != '15.0':
        raise Warning('Module support Odoo series 15.0 found {}.'.format(version_info))
    return True



