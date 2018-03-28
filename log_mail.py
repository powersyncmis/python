# -*- coding: utf8 -*-
import logging
import logging.handlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.ERROR)
handler = logging.handlers.SMTPHandler(
    mailhost='ns3.powersync.com.tw',
    fromaddr='tp_pf01@powersync.com.tw',
    toaddrs='tp_pf01@powersync.com.tw',
    subject="Houston, We've Got a Problem",
    credentials=('tp_pf01', 'power&mis')
)
rootLogger.addHandler(handler)

log = logging.getLogger(__name__)
log.fatal('HELP! We are under attack!')
