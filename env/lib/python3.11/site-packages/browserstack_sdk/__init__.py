# coding: UTF-8
import sys
bstack1ll_opy_ = sys.version_info [0] == 2
bstackl_opy_ = 2048
bstack111_opy_ = 7
def bstack1l1_opy_ (bstack1l1l_opy_):
    global bstack11_opy_
    stringNr = ord (bstack1l1l_opy_ [-1])
    bstack1_opy_ = bstack1l1l_opy_ [:-1]
    bstack11l_opy_ = stringNr % len (bstack1_opy_)
    bstack1lll_opy_ = bstack1_opy_ [:bstack11l_opy_] + bstack1_opy_ [bstack11l_opy_:]
    if bstack1ll_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstackl_opy_ - (bstack1l_opy_ + stringNr) % bstack111_opy_) for bstack1l_opy_, char in enumerate (bstack1lll_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstackl_opy_ - (bstack1l_opy_ + stringNr) % bstack111_opy_) for bstack1l_opy_, char in enumerate (bstack1lll_opy_)])
    return eval (bstack1ll1_opy_)
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
from packaging import version
from browserstack.local import Local
bstack11ll1_opy_ = {
	bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ে"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩৈ"),
  bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ৉"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪ৊"),
  bstack1l1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫো"): bstack1l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ৌ"),
  bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅ্ࠪ"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫৎ"),
  bstack1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ৏"): bstack1l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧ৐"),
  bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ৑"): bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧ৒"),
  bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ৓"): bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ৔"),
  bstack1l1_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪ৕"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪ৖"),
  bstack1l1_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫৗ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧ৘"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭৙"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭৚"),
  bstack1l1_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧ৛"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧড়"),
  bstack1l1_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫঢ়"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫ৞"),
  bstack1l1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭য়"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ৠ"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩৡ"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩৢ"),
  bstack1l1_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩৣ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩ৤"),
  bstack1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ৥"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ০"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ১"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ২"),
  bstack1l1_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ৩"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩ৪"),
  bstack1l1_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ৫"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪ৬"),
  bstack1l1_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ৭"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧ৮"),
  bstack1l1_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫ৯"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫৰ"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ৱ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭৲"),
  bstack1l1_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬ৳"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬ৴"),
  bstack1l1_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩ৵"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩ৶"),
  bstack1l1_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ৷"): bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ৸"),
  bstack1l1_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ৹"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ৺"),
  bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ৻"): bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨৼ"),
  bstack1l1_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭৽"): bstack1l1_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨ৾"),
  bstack1l1_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ৿"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ਀"),
  bstack1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭ਁ"): bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭ਂ"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩਃ"): bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ਄"),
  bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩਅ"): bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬਆ"),
  bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧਇ"): bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧਈ"),
  bstack1l1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧਉ"): bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧਊ"),
  bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ਋"): bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ਌"),
  bstack1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭਍"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭਎"),
}
bstack1ll11_opy_ = [
  bstack1l1_opy_ (u"࠭࡯ࡴࠩਏ"),
  bstack1l1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪਐ"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ਑"),
  bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ਒"),
  bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧਓ"),
  bstack1l1_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨਔ"),
  bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬਕ"),
]
bstack1l111_opy_ = {
  bstack1l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩਖ"): bstack1l1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫਗ"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪਘ"): [bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫਙ"), bstack1l1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ਚ")],
  bstack1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਛ"): bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪਜ"),
  bstack1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪਝ"): bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧਞ"),
  bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ਟ"): [bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪਠ"), bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩਡ")],
  bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬਢ"): bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧਣ"),
  bstack1l1_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪਤ"): bstack1l1_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬਥ"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨਦ"): [bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩਧ"), bstack1l1_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫਨ")],
  bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪ਩"): [bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭ਪ"), bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹ࠭ਫ")]
}
bstack11111_opy_ = {
  bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭ਬ"): [bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡶࡴࡔࡵ࡯ࡇࡪࡸࡴࡴࠩਭ"), bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡕࡶࡰࡈ࡫ࡲࡵࠩਮ")]
}
bstack1l11l_opy_ = [
  bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩਯ"),
  bstack1l1_opy_ (u"ࠫࡵࡧࡧࡦࡎࡲࡥࡩ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠧਰ"),
  bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ਱"),
  bstack1l1_opy_ (u"࠭ࡳࡦࡶ࡚࡭ࡳࡪ࡯ࡸࡔࡨࡧࡹ࠭ਲ"),
  bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡴࡻࡴࡴࠩਲ਼"),
  bstack1l1_opy_ (u"ࠨࡵࡷࡶ࡮ࡩࡴࡇ࡫࡯ࡩࡎࡴࡴࡦࡴࡤࡧࡹࡧࡢࡪ࡮࡬ࡸࡾ࠭਴"),
  bstack1l1_opy_ (u"ࠩࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡕࡸ࡯࡮ࡲࡷࡆࡪ࡮ࡡࡷ࡫ࡲࡶࠬਵ"),
  bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨਸ਼"),
  bstack1l1_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩ਷"),
  bstack1l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ਸ"),
  bstack1l1_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬਹ"),
  bstack1l1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ਺"),
]
bstack1llll1_opy_ = [
  bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ਻"),
  bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ਼࠭"),
  bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ਽"),
  bstack1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫਾ"),
  bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨਿ"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨੀ"),
  bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪੁ"),
  bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬੂ"),
  bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ੃"),
]
bstack1ll1l_opy_ = [
  bstack1l1_opy_ (u"ࠪࡹࡵࡲ࡯ࡢࡦࡐࡩࡩ࡯ࡡࠨ੄"),
  bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭੅"),
  bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ੆"),
  bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੇ"),
  bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡕࡸࡩࡰࡴ࡬ࡸࡾ࠭ੈ"),
  bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ੉"),
  bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡕࡣࡪࠫ੊"),
  bstack1l1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨੋ"),
  bstack1l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ੌ"),
  bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧ੍ࠪ"),
  bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ੎"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭੏"),
  bstack1l1_opy_ (u"ࠨࡱࡶࠫ੐"),
  bstack1l1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬੑ"),
  bstack1l1_opy_ (u"ࠪ࡬ࡴࡹࡴࡴࠩ੒"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭੓"),
  bstack1l1_opy_ (u"ࠬࡸࡥࡨ࡫ࡲࡲࠬ੔"),
  bstack1l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨ੕"),
  bstack1l1_opy_ (u"ࠧ࡮ࡣࡦ࡬࡮ࡴࡥࠨ੖"),
  bstack1l1_opy_ (u"ࠨࡴࡨࡷࡴࡲࡵࡵ࡫ࡲࡲࠬ੗"),
  bstack1l1_opy_ (u"ࠩ࡬ࡨࡱ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ੘"),
  bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧਖ਼"),
  bstack1l1_opy_ (u"ࠫࡻ࡯ࡤࡦࡱࠪਗ਼"),
  bstack1l1_opy_ (u"ࠬࡴ࡯ࡑࡣࡪࡩࡑࡵࡡࡥࡖ࡬ࡱࡪࡵࡵࡵࠩਜ਼"),
  bstack1l1_opy_ (u"࠭ࡢࡧࡥࡤࡧ࡭࡫ࠧੜ"),
  bstack1l1_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭੝"),
  bstack1l1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡔࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬਫ਼"),
  bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡨࡲࡩࡑࡥࡺࡵࠪ੟"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡧ࡬ࡎࡱࡥ࡭ࡱ࡫ࠧ੠"),
  bstack1l1_opy_ (u"ࠫࡳࡵࡐࡪࡲࡨࡰ࡮ࡴࡥࠨ੡"),
  bstack1l1_opy_ (u"ࠬࡩࡨࡦࡥ࡮࡙ࡗࡒࠧ੢"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੣"),
  bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡃࡰࡱ࡮࡭ࡪࡹࠧ੤"),
  bstack1l1_opy_ (u"ࠨࡥࡤࡴࡹࡻࡲࡦࡅࡵࡥࡸ࡮ࠧ੥"),
  bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭੦"),
  bstack1l1_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ੧"),
  bstack1l1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ੨"),
  bstack1l1_opy_ (u"ࠬࡴ࡯ࡃ࡮ࡤࡲࡰࡖ࡯࡭࡮࡬ࡲ࡬࠭੩"),
  bstack1l1_opy_ (u"࠭࡭ࡢࡵ࡮ࡗࡪࡴࡤࡌࡧࡼࡷࠬ੪"),
  bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡌࡰࡩࡶࠫ੫"),
  bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡊࡦࠪ੬"),
  bstack1l1_opy_ (u"ࠩࡧࡩࡩ࡯ࡣࡢࡶࡨࡨࡉ࡫ࡶࡪࡥࡨࠫ੭"),
  bstack1l1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡓࡥࡷࡧ࡭ࡴࠩ੮"),
  bstack1l1_opy_ (u"ࠫࡵ࡮࡯࡯ࡧࡑࡹࡲࡨࡥࡳࠩ੯"),
  bstack1l1_opy_ (u"ࠬࡴࡥࡵࡹࡲࡶࡰࡒ࡯ࡨࡵࠪੰ"),
  bstack1l1_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡓࡵࡺࡩࡰࡰࡶࠫੱ"),
  bstack1l1_opy_ (u"ࠧࡤࡱࡱࡷࡴࡲࡥࡍࡱࡪࡷࠬੲ"),
  bstack1l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨੳ"),
  bstack1l1_opy_ (u"ࠩࡤࡴࡵ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭ੴ"),
  bstack1l1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡅ࡭ࡴࡳࡥࡵࡴ࡬ࡧࠬੵ"),
  bstack1l1_opy_ (u"ࠫࡻ࡯ࡤࡦࡱ࡙࠶ࠬ੶"),
  bstack1l1_opy_ (u"ࠬࡳࡩࡥࡕࡨࡷࡸ࡯࡯࡯ࡋࡱࡷࡹࡧ࡬࡭ࡃࡳࡴࡸ࠭੷"),
  bstack1l1_opy_ (u"࠭ࡥࡴࡲࡵࡩࡸࡹ࡯ࡔࡧࡵࡺࡪࡸࠧ੸"),
  bstack1l1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭੹"),
  bstack1l1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࡆࡨࡵ࠭੺"),
  bstack1l1_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩ੻"),
  bstack1l1_opy_ (u"ࠪࡷࡾࡴࡣࡕ࡫ࡰࡩ࡜࡯ࡴࡩࡐࡗࡔࠬ੼"),
  bstack1l1_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩ੽"),
  bstack1l1_opy_ (u"ࠬ࡭ࡰࡴࡎࡲࡧࡦࡺࡩࡰࡰࠪ੾"),
  bstack1l1_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡐࡳࡱࡩ࡭ࡱ࡫ࠧ੿"),
  bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡎࡦࡶࡺࡳࡷࡱࠧ઀"),
  bstack1l1_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࡃࡩࡣࡱ࡫ࡪࡐࡡࡳࠩઁ"),
  bstack1l1_opy_ (u"ࠩࡻࡱࡸࡐࡡࡳࠩં"),
  bstack1l1_opy_ (u"ࠪࡼࡲࡾࡊࡢࡴࠪઃ"),
  bstack1l1_opy_ (u"ࠫࡲࡧࡳ࡬ࡅࡲࡱࡲࡧ࡮ࡥࡵࠪ઄"),
  bstack1l1_opy_ (u"ࠬࡳࡡࡴ࡭ࡅࡥࡸ࡯ࡣࡂࡷࡷ࡬ࠬઅ"),
  bstack1l1_opy_ (u"࠭ࡷࡴࡎࡲࡧࡦࡲࡓࡶࡲࡳࡳࡷࡺࠧઆ"),
  bstack1l1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡄࡱࡵࡷࡗ࡫ࡳࡵࡴ࡬ࡧࡹ࡯࡯࡯ࡵࠪઇ"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴ࡛࡫ࡲࡴ࡫ࡲࡲࠬઈ"),
  bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡰࡵࡋࡱࡷࡪࡩࡵࡳࡧࡆࡩࡷࡺࡳࠨઉ"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡹࡩࡨࡰࡄࡴࡵ࠭ઊ"),
  bstack1l1_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡩ࡮ࡣࡷ࡭ࡴࡴࡳࠨઋ"),
  bstack1l1_opy_ (u"ࠬࡩࡡ࡯ࡣࡵࡽࠬઌ"),
  bstack1l1_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧઍ"),
  bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ઎"),
  bstack1l1_opy_ (u"ࠨ࡫ࡨࠫએ"),
  bstack1l1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧઐ"),
  bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪઑ"),
  bstack1l1_opy_ (u"ࠫࡶࡻࡥࡶࡧࠪ઒"),
  bstack1l1_opy_ (u"ࠬ࡯࡮ࡵࡧࡵࡲࡦࡲࠧઓ"),
  bstack1l1_opy_ (u"࠭ࡡࡱࡲࡖࡸࡴࡸࡥࡄࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠧઔ"),
  bstack1l1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡃࡢ࡯ࡨࡶࡦࡏ࡭ࡢࡩࡨࡍࡳࡰࡥࡤࡶ࡬ࡳࡳ࠭ક"),
  bstack1l1_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸࡋࡸࡤ࡮ࡸࡨࡪࡎ࡯ࡴࡶࡶࠫખ"),
  bstack1l1_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡏࡳ࡬ࡹࡉ࡯ࡥ࡯ࡹࡩ࡫ࡈࡰࡵࡷࡷࠬગ"),
  bstack1l1_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡄࡴࡵ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧઘ"),
  bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡦࡴࡹࡩࡉ࡫ࡶࡪࡥࡨࠫઙ"),
  bstack1l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬચ"),
  bstack1l1_opy_ (u"࠭ࡳࡦࡰࡧࡏࡪࡿࡳࠨછ"),
  bstack1l1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡐࡢࡵࡶࡧࡴࡪࡥࠨજ"),
  bstack1l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡷࡧ࡭ࡴࡏ࡮࡫ࡧࡦࡸ࡮ࡵ࡮ࠨઝ"),
  bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪઞ"),
  bstack1l1_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨટ"),
  bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ઠ"),
  bstack1l1_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩડ"),
  bstack1l1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡖࡲࡦࡨࡨࡶࡪࡴࡣࡦࡵࠪઢ"),
  bstack1l1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡓࡪ࡯ࠪણ"),
  bstack1l1_opy_ (u"ࠨࡴࡨࡱࡴࡼࡥࡊࡑࡖࡅࡵࡶࡓࡦࡶࡷ࡭ࡳ࡭ࡳࡍࡱࡦࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ત"),
  bstack1l1_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫથ"),
  bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")
]
bstack1111l_opy_ = {
  bstack1l1_opy_ (u"ࠫࡻ࠭ધ"): bstack1l1_opy_ (u"ࠬࡼࠧન"),
  bstack1l1_opy_ (u"࠭ࡦࠨ઩"): bstack1l1_opy_ (u"ࠧࡧࠩપ"),
  bstack1l1_opy_ (u"ࠨࡨࡲࡶࡨ࡫ࠧફ"): bstack1l1_opy_ (u"ࠩࡩࡳࡷࡩࡥࠨબ"),
  bstack1l1_opy_ (u"ࠪࡳࡳࡲࡹࡢࡷࡷࡳࡲࡧࡴࡦࠩભ"): bstack1l1_opy_ (u"ࠫࡴࡴ࡬ࡺࡃࡸࡸࡴࡳࡡࡵࡧࠪમ"),
  bstack1l1_opy_ (u"ࠬ࡬࡯ࡳࡥࡨࡰࡴࡩࡡ࡭ࠩય"): bstack1l1_opy_ (u"࠭ࡦࡰࡴࡦࡩࡱࡵࡣࡢ࡮ࠪર"),
  bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡮࡯ࡴࡶࠪ઱"): bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫલ"),
  bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡱࡱࡵࡸࠬળ"): bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭઴"),
  bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡸࡷࡪࡸࠧવ"): bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨશ"),
  bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡵࡧࡳࡴࠩષ"): bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪસ"),
  bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽ࡭ࡵࡳࡵࠩહ"): bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾࡎ࡯ࡴࡶࠪ઺"),
  bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡰࡰࡴࡷࠫ઻"): bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡱࡵࡸ઼ࠬ"),
  bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡷࡶࡩࡷ࠭ઽ"): bstack1l1_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡖࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨા"),
  bstack1l1_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩિ"): bstack1l1_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪી"),
  bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡱࡴࡲࡼࡾࡶࡡࡴࡵࠪુ"): bstack1l1_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬૂ"),
  bstack1l1_opy_ (u"ࠫ࠲ࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡤࡷࡸ࠭ૃ"): bstack1l1_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧૄ"),
  bstack1l1_opy_ (u"࠭ࡢࡪࡰࡤࡶࡾࡶࡡࡵࡪࠪૅ"): bstack1l1_opy_ (u"ࠧࡣ࡫ࡱࡥࡷࡿࡰࡢࡶ࡫ࠫ૆"),
  bstack1l1_opy_ (u"ࠨࡲࡤࡧ࡫࡯࡬ࡦࠩે"): bstack1l1_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬૈ"),
  bstack1l1_opy_ (u"ࠪࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬૉ"): bstack1l1_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ૊"),
  bstack1l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨો"): bstack1l1_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩૌ"),
  bstack1l1_opy_ (u"ࠧ࡭ࡱࡪࡪ࡮ࡲࡥࠨ્"): bstack1l1_opy_ (u"ࠨ࡮ࡲ࡫࡫࡯࡬ࡦࠩ૎"),
  bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏"): bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૐ"),
}
bstack1l1l1_opy_ = bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡽࡤ࠰ࡪࡸࡦࠬ૑")
bstack11l1l_opy_ = bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࡮ࡵࡣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠨ૒")
bstack11l11_opy_ = {
  bstack1l1_opy_ (u"࠭ࡣࡳ࡫ࡷ࡭ࡨࡧ࡬ࠨ૓"): 50,
  bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭૔"): 40,
  bstack1l1_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩ૕"): 30,
  bstack1l1_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ૖"): 20,
  bstack1l1_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩ૗"): 10
}
DEFAULT_LOG_LEVEL = bstack11l11_opy_[bstack1l1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ૘")]
bstack1lll1_opy_ = bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫ૙")
bstack111l_opy_ = bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࠫ૚")
bstack11lll_opy_ = bstack1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴࠭૛")
bstack111l1_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧ૜")
bstack1l11_opy_ = [bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ૝"), bstack1l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ૞")]
bstack11l1_opy_ = [bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧ૟"), bstack1l1_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧૠ")]
bstack1lll11_opy_ = [
  bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡑࡥࡲ࡫ࠧૡ"),
  bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩૢ"),
  bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬૣ"),
  bstack1l1_opy_ (u"ࠩࡱࡩࡼࡉ࡯࡮࡯ࡤࡲࡩ࡚ࡩ࡮ࡧࡲࡹࡹ࠭૤"),
  bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧ૥"),
  bstack1l1_opy_ (u"ࠫࡺࡪࡩࡥࠩ૦"),
  bstack1l1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ૧"),
  bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࠭૨"),
  bstack1l1_opy_ (u"ࠧࡰࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬ૩"),
  bstack1l1_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࠭૪"),
  bstack1l1_opy_ (u"ࠩࡱࡳࡗ࡫ࡳࡦࡶࠪ૫"), bstack1l1_opy_ (u"ࠪࡪࡺࡲ࡬ࡓࡧࡶࡩࡹ࠭૬"),
  bstack1l1_opy_ (u"ࠫࡨࡲࡥࡢࡴࡖࡽࡸࡺࡥ࡮ࡈ࡬ࡰࡪࡹࠧ૭"),
  bstack1l1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡘ࡮ࡳࡩ࡯ࡩࡶࠫ૮"),
  bstack1l1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࡏࡳ࡬࡭ࡩ࡯ࡩࠪ૯"),
  bstack1l1_opy_ (u"ࠧࡰࡶ࡫ࡩࡷࡇࡰࡱࡵࠪ૰"),
  bstack1l1_opy_ (u"ࠨࡲࡵ࡭ࡳࡺࡐࡢࡩࡨࡗࡴࡻࡲࡤࡧࡒࡲࡋ࡯࡮ࡥࡈࡤ࡭ࡱࡻࡲࡦࠩ૱"),
  bstack1l1_opy_ (u"ࠩࡤࡴࡵࡇࡣࡵ࡫ࡹ࡭ࡹࡿࠧ૲"), bstack1l1_opy_ (u"ࠪࡥࡵࡶࡐࡢࡥ࡮ࡥ࡬࡫ࠧ૳"), bstack1l1_opy_ (u"ࠫࡦࡶࡰࡘࡣ࡬ࡸࡆࡩࡴࡪࡸ࡬ࡸࡾ࠭૴"), bstack1l1_opy_ (u"ࠬࡧࡰࡱ࡙ࡤ࡭ࡹࡖࡡࡤ࡭ࡤ࡫ࡪ࠭૵"), bstack1l1_opy_ (u"࠭ࡡࡱࡲ࡚ࡥ࡮ࡺࡄࡶࡴࡤࡸ࡮ࡵ࡮ࠨ૶"),
  bstack1l1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬ૷"),
  bstack1l1_opy_ (u"ࠨࡣ࡯ࡰࡴࡽࡔࡦࡵࡷࡔࡦࡩ࡫ࡢࡩࡨࡷࠬ૸"),
  bstack1l1_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡆࡳࡻ࡫ࡲࡢࡩࡨࠫૹ"), bstack1l1_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡇࡴࡼࡥࡳࡣࡪࡩࡊࡴࡤࡊࡰࡷࡩࡳࡺࠧૺ"),
  bstack1l1_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡉ࡫ࡶࡪࡥࡨࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩૻ"),
  bstack1l1_opy_ (u"ࠬࡧࡤࡣࡒࡲࡶࡹ࠭ૼ"),
  bstack1l1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡄࡦࡸ࡬ࡧࡪ࡙࡯ࡤ࡭ࡨࡸࠬ૽"),
  bstack1l1_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡊࡰࡶࡸࡦࡲ࡬ࡕ࡫ࡰࡩࡴࡻࡴࠨ૾"),
  bstack1l1_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡋࡱࡷࡹࡧ࡬࡭ࡒࡤࡸ࡭࠭૿"),
  bstack1l1_opy_ (u"ࠩࡤࡺࡩ࠭଀"), bstack1l1_opy_ (u"ࠪࡥࡻࡪࡌࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ଁ"), bstack1l1_opy_ (u"ࠫࡦࡼࡤࡓࡧࡤࡨࡾ࡚ࡩ࡮ࡧࡲࡹࡹ࠭ଂ"), bstack1l1_opy_ (u"ࠬࡧࡶࡥࡃࡵ࡫ࡸ࠭ଃ"),
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡎࡩࡾࡹࡴࡰࡴࡨࠫ଄"), bstack1l1_opy_ (u"ࠧ࡬ࡧࡼࡷࡹࡵࡲࡦࡒࡤࡸ࡭࠭ଅ"), bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࡸࡺ࡯ࡳࡧࡓࡥࡸࡹࡷࡰࡴࡧࠫଆ"),
  bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡇ࡬ࡪࡣࡶࠫଇ"), bstack1l1_opy_ (u"ࠪ࡯ࡪࡿࡐࡢࡵࡶࡻࡴࡸࡤࠨଈ"),
  bstack1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡈࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠭ଉ"), bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡅࡷ࡭ࡳࠨଊ"), bstack1l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࡅ࡫ࡵࠫଋ"), bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡉࡨࡳࡱࡰࡩࡒࡧࡰࡱ࡫ࡱ࡫ࡋ࡯࡬ࡦࠩଌ"), bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡕࡴࡧࡖࡽࡸࡺࡥ࡮ࡇࡻࡩࡨࡻࡴࡢࡤ࡯ࡩࠬ଍"),
  bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡑࡱࡵࡸࠬ଎"), bstack1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡒࡲࡶࡹࡹࠧଏ"),
  bstack1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡇ࡭ࡸࡧࡢ࡭ࡧࡅࡹ࡮ࡲࡤࡄࡪࡨࡧࡰ࠭ଐ"),
  bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱ࡚ࡩࡧࡼࡩࡦࡹࡗ࡭ࡲ࡫࡯ࡶࡶࠪ଑"),
  bstack1l1_opy_ (u"࠭ࡩ࡯ࡶࡨࡲࡹࡇࡣࡵ࡫ࡲࡲࠬ଒"), bstack1l1_opy_ (u"ࠧࡪࡰࡷࡩࡳࡺࡃࡢࡶࡨ࡫ࡴࡸࡹࠨଓ"), bstack1l1_opy_ (u"ࠨ࡫ࡱࡸࡪࡴࡴࡇ࡮ࡤ࡫ࡸ࠭ଔ"), bstack1l1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡣ࡯ࡍࡳࡺࡥ࡯ࡶࡄࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬକ"),
  bstack1l1_opy_ (u"ࠪࡨࡴࡴࡴࡔࡶࡲࡴࡆࡶࡰࡐࡰࡕࡩࡸ࡫ࡴࠨଖ"),
  bstack1l1_opy_ (u"ࠫࡺࡴࡩࡤࡱࡧࡩࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭ଗ"), bstack1l1_opy_ (u"ࠬࡸࡥࡴࡧࡷࡏࡪࡿࡢࡰࡣࡵࡨࠬଘ"),
  bstack1l1_opy_ (u"࠭࡮ࡰࡕ࡬࡫ࡳ࠭ଙ"),
  bstack1l1_opy_ (u"ࠧࡪࡩࡱࡳࡷ࡫ࡕ࡯࡫ࡰࡴࡴࡸࡴࡢࡰࡷ࡚࡮࡫ࡷࡴࠩଚ"),
  bstack1l1_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡱࡨࡷࡵࡩࡥ࡙ࡤࡸࡨ࡮ࡥࡳࡵࠪଛ"),
  bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଜ"),
  bstack1l1_opy_ (u"ࠪࡶࡪࡩࡲࡦࡣࡷࡩࡈ࡮ࡲࡰ࡯ࡨࡈࡷ࡯ࡶࡦࡴࡖࡩࡸࡹࡩࡰࡰࡶࠫଝ"),
  bstack1l1_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨ࡛ࡪࡨࡓࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪଞ"),
  bstack1l1_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡒࡤࡸ࡭࠭ଟ"),
  bstack1l1_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡓࡱࡧࡨࡨࠬଠ"),
  bstack1l1_opy_ (u"ࠧࡨࡲࡶࡉࡳࡧࡢ࡭ࡧࡧࠫଡ"),
  bstack1l1_opy_ (u"ࠨ࡫ࡶࡌࡪࡧࡤ࡭ࡧࡶࡷࠬଢ"),
  bstack1l1_opy_ (u"ࠩࡤࡨࡧࡋࡸࡦࡥࡗ࡭ࡲ࡫࡯ࡶࡶࠪଣ"),
  bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡧࡖࡧࡷ࡯ࡰࡵࠩତ"),
  bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡆࡨࡺ࡮ࡩࡥࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨଥ"),
  bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡊࡶࡦࡴࡴࡑࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷࠬଦ"),
  bstack1l1_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡎࡢࡶࡸࡶࡦࡲࡏࡳ࡫ࡨࡲࡹࡧࡴࡪࡱࡱࠫଧ"),
  bstack1l1_opy_ (u"ࠧࡴࡻࡶࡸࡪࡳࡐࡰࡴࡷࠫନ"),
  bstack1l1_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡂࡦࡥࡌࡴࡹࡴࠨ଩"),
  bstack1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡕ࡯࡮ࡲࡧࡰ࠭ପ"), bstack1l1_opy_ (u"ࠪࡹࡳࡲ࡯ࡤ࡭ࡗࡽࡵ࡫ࠧଫ"), bstack1l1_opy_ (u"ࠫࡺࡴ࡬ࡰࡥ࡮ࡏࡪࡿࠧବ"),
  bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡏࡥࡺࡴࡣࡩࠩଭ"),
  bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡣࡢࡶࡆࡥࡵࡺࡵࡳࡧࠪମ"),
  bstack1l1_opy_ (u"ࠧࡶࡰ࡬ࡲࡸࡺࡡ࡭࡮ࡒࡸ࡭࡫ࡲࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠩଯ"),
  bstack1l1_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦ࡙࡬ࡲࡩࡵࡷࡂࡰ࡬ࡱࡦࡺࡩࡰࡰࠪର"),
  bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡕࡱࡲࡰࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭଱"),
  bstack1l1_opy_ (u"ࠪࡩࡳ࡬࡯ࡳࡥࡨࡅࡵࡶࡉ࡯ࡵࡷࡥࡱࡲࠧଲ"),
  bstack1l1_opy_ (u"ࠫࡪࡴࡳࡶࡴࡨ࡛ࡪࡨࡶࡪࡧࡺࡷࡍࡧࡶࡦࡒࡤ࡫ࡪࡹࠧଳ"), bstack1l1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼࡊࡥࡷࡶࡲࡳࡱࡹࡐࡰࡴࡷࠫ଴"), bstack1l1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪ࡝ࡥࡣࡸ࡬ࡩࡼࡊࡥࡵࡣ࡬ࡰࡸࡉ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠩଵ"),
  bstack1l1_opy_ (u"ࠧࡳࡧࡰࡳࡹ࡫ࡁࡱࡲࡶࡇࡦࡩࡨࡦࡎ࡬ࡱ࡮ࡺࠧଶ"),
  bstack1l1_opy_ (u"ࠨࡥࡤࡰࡪࡴࡤࡢࡴࡉࡳࡷࡳࡡࡵࠩଷ"),
  bstack1l1_opy_ (u"ࠩࡥࡹࡳࡪ࡬ࡦࡋࡧࠫସ"),
  bstack1l1_opy_ (u"ࠪࡰࡦࡻ࡮ࡤࡪࡗ࡭ࡲ࡫࡯ࡶࡶࠪହ"),
  bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࡙ࡥࡳࡸ࡬ࡧࡪࡹࡅ࡯ࡣࡥࡰࡪࡪࠧ଺"), bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࡓࡦࡴࡹ࡭ࡨ࡫ࡳࡂࡷࡷ࡬ࡴࡸࡩࡻࡧࡧࠫ଻"),
  bstack1l1_opy_ (u"࠭ࡡࡶࡶࡲࡅࡨࡩࡥࡱࡶࡄࡰࡪࡸࡴࡴ଼ࠩ"), bstack1l1_opy_ (u"ࠧࡢࡷࡷࡳࡉ࡯ࡳ࡮࡫ࡶࡷࡆࡲࡥࡳࡶࡶࠫଽ"),
  bstack1l1_opy_ (u"ࠨࡰࡤࡸ࡮ࡼࡥࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡷࡑ࡯ࡢࠨା"),
  bstack1l1_opy_ (u"ࠩࡱࡥࡹ࡯ࡶࡦ࡙ࡨࡦ࡙ࡧࡰࠨି"),
  bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡌࡲ࡮ࡺࡩࡢ࡮ࡘࡶࡱ࠭ୀ"), bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࡅࡱࡲ࡯ࡸࡒࡲࡴࡺࡶࡳࠨୁ"), bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࡎ࡭࡮ࡰࡴࡨࡊࡷࡧࡵࡥ࡙ࡤࡶࡳ࡯࡮ࡨࠩୂ"), bstack1l1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡦࡰࡏ࡭ࡳࡱࡳࡊࡰࡅࡥࡨࡱࡧࡳࡱࡸࡲࡩ࠭ୃ"),
  bstack1l1_opy_ (u"ࠧ࡬ࡧࡨࡴࡐ࡫ࡹࡄࡪࡤ࡭ࡳࡹࠧୄ"),
  bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡩࡻࡣࡥࡰࡪ࡙ࡴࡳ࡫ࡱ࡫ࡸࡊࡩࡳࠩ୅"),
  bstack1l1_opy_ (u"ࠩࡳࡶࡴࡩࡥࡴࡵࡄࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ୆"),
  bstack1l1_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡍࡨࡽࡉ࡫࡬ࡢࡻࠪେ"),
  bstack1l1_opy_ (u"ࠫࡸ࡮࡯ࡸࡋࡒࡗࡑࡵࡧࠨୈ"),
  bstack1l1_opy_ (u"ࠬࡹࡥ࡯ࡦࡎࡩࡾ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠧ୉"),
  bstack1l1_opy_ (u"࠭ࡷࡦࡤ࡮࡭ࡹࡘࡥࡴࡲࡲࡲࡸ࡫ࡔࡪ࡯ࡨࡳࡺࡺࠧ୊"), bstack1l1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷ࡛ࡦ࡯ࡴࡕ࡫ࡰࡩࡴࡻࡴࠨୋ"),
  bstack1l1_opy_ (u"ࠨࡴࡨࡱࡴࡺࡥࡅࡧࡥࡹ࡬ࡖࡲࡰࡺࡼࠫୌ"),
  bstack1l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡃࡶࡽࡳࡩࡅࡹࡧࡦࡹࡹ࡫ࡆࡳࡱࡰࡌࡹࡺࡰࡴ୍ࠩ"),
  bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡍࡱࡪࡇࡦࡶࡴࡶࡴࡨࠫ୎"),
  bstack1l1_opy_ (u"ࠫࡼ࡫ࡢ࡬࡫ࡷࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࡐࡰࡴࡷࠫ୏"),
  bstack1l1_opy_ (u"ࠬ࡬ࡵ࡭࡮ࡆࡳࡳࡺࡥࡹࡶࡏ࡭ࡸࡺࠧ୐"),
  bstack1l1_opy_ (u"࠭ࡷࡢ࡫ࡷࡊࡴࡸࡁࡱࡲࡖࡧࡷ࡯ࡰࡵࠩ୑"),
  bstack1l1_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࡄࡱࡱࡲࡪࡩࡴࡓࡧࡷࡶ࡮࡫ࡳࠨ୒"),
  bstack1l1_opy_ (u"ࠨࡣࡳࡴࡓࡧ࡭ࡦࠩ୓"),
  bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡕࡖࡐࡈ࡫ࡲࡵࠩ୔"),
  bstack1l1_opy_ (u"ࠪࡸࡦࡶࡗࡪࡶ࡫ࡗ࡭ࡵࡲࡵࡒࡵࡩࡸࡹࡄࡶࡴࡤࡸ࡮ࡵ࡮ࠨ୕"),
  bstack1l1_opy_ (u"ࠫࡸࡩࡡ࡭ࡧࡉࡥࡨࡺ࡯ࡳࠩୖ"),
  bstack1l1_opy_ (u"ࠬࡽࡤࡢࡎࡲࡧࡦࡲࡐࡰࡴࡷࠫୗ"),
  bstack1l1_opy_ (u"࠭ࡳࡩࡱࡺ࡜ࡨࡵࡤࡦࡎࡲ࡫ࠬ୘"),
  bstack1l1_opy_ (u"ࠧࡪࡱࡶࡍࡳࡹࡴࡢ࡮࡯ࡔࡦࡻࡳࡦࠩ୙"),
  bstack1l1_opy_ (u"ࠨࡺࡦࡳࡩ࡫ࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠪ୚"),
  bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡹࡳࡸࡱࡵࡨࠬ୛"),
  bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡐࡳࡧࡥࡹ࡮ࡲࡴࡘࡆࡄࠫଡ଼"),
  bstack1l1_opy_ (u"ࠫࡵࡸࡥࡷࡧࡱࡸ࡜ࡊࡁࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠬଢ଼"),
  bstack1l1_opy_ (u"ࠬࡽࡥࡣࡆࡵ࡭ࡻ࡫ࡲࡂࡩࡨࡲࡹ࡛ࡲ࡭ࠩ୞"),
  bstack1l1_opy_ (u"࠭࡫ࡦࡻࡦ࡬ࡦ࡯࡮ࡑࡣࡷ࡬ࠬୟ"),
  bstack1l1_opy_ (u"ࠧࡶࡵࡨࡒࡪࡽࡗࡅࡃࠪୠ"),
  bstack1l1_opy_ (u"ࠨࡹࡧࡥࡑࡧࡵ࡯ࡥ࡫ࡘ࡮ࡳࡥࡰࡷࡷࠫୡ"), bstack1l1_opy_ (u"ࠩࡺࡨࡦࡉ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࡖ࡬ࡱࡪࡵࡵࡵࠩୢ"),
  bstack1l1_opy_ (u"ࠪࡼࡨࡵࡤࡦࡑࡵ࡫ࡎࡪࠧୣ"), bstack1l1_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡖ࡭࡬ࡴࡩ࡯ࡩࡌࡨࠬ୤"),
  bstack1l1_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩ࡝ࡄࡂࡄࡸࡲࡩࡲࡥࡊࡦࠪ୥"),
  bstack1l1_opy_ (u"࠭ࡲࡦࡵࡨࡸࡔࡴࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡵࡸࡔࡴ࡬ࡺࠩ୦"),
  bstack1l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡕ࡫ࡰࡩࡴࡻࡴࡴࠩ୧"),
  bstack1l1_opy_ (u"ࠨࡹࡧࡥࡘࡺࡡࡳࡶࡸࡴࡗ࡫ࡴࡳ࡫ࡨࡷࠬ୨"), bstack1l1_opy_ (u"ࠩࡺࡨࡦ࡙ࡴࡢࡴࡷࡹࡵࡘࡥࡵࡴࡼࡍࡳࡺࡥࡳࡸࡤࡰࠬ୩"),
  bstack1l1_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࡌࡦࡸࡤࡸࡣࡵࡩࡐ࡫ࡹࡣࡱࡤࡶࡩ࠭୪"),
  bstack1l1_opy_ (u"ࠫࡲࡧࡸࡕࡻࡳ࡭ࡳ࡭ࡆࡳࡧࡴࡹࡪࡴࡣࡺࠩ୫"),
  bstack1l1_opy_ (u"ࠬࡹࡩ࡮ࡲ࡯ࡩࡎࡹࡖࡪࡵ࡬ࡦࡱ࡫ࡃࡩࡧࡦ࡯ࠬ୬"),
  bstack1l1_opy_ (u"࠭ࡵࡴࡧࡆࡥࡷࡺࡨࡢࡩࡨࡗࡸࡲࠧ୭"),
  bstack1l1_opy_ (u"ࠧࡴࡪࡲࡹࡱࡪࡕࡴࡧࡖ࡭ࡳ࡭࡬ࡦࡶࡲࡲ࡙࡫ࡳࡵࡏࡤࡲࡦ࡭ࡥࡳࠩ୮"),
  bstack1l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡉࡘࡆࡓࠫ୯"),
  bstack1l1_opy_ (u"ࠩࡤࡰࡱࡵࡷࡕࡱࡸࡧ࡭ࡏࡤࡆࡰࡵࡳࡱࡲࠧ୰"),
  bstack1l1_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡋ࡭ࡩࡪࡥ࡯ࡃࡳ࡭ࡕࡵ࡬ࡪࡥࡼࡉࡷࡸ࡯ࡳࠩୱ"),
  bstack1l1_opy_ (u"ࠫࡲࡵࡣ࡬ࡎࡲࡧࡦࡺࡩࡰࡰࡄࡴࡵ࠭୲"),
  bstack1l1_opy_ (u"ࠬࡲ࡯ࡨࡥࡤࡸࡋࡵࡲ࡮ࡣࡷࠫ୳"), bstack1l1_opy_ (u"࠭࡬ࡰࡩࡦࡥࡹࡌࡩ࡭ࡶࡨࡶࡘࡶࡥࡤࡵࠪ୴"),
  bstack1l1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡊࡥ࡭ࡣࡼࡅࡩࡨࠧ୵")
]
bstack1l1ll_opy_ = bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡶࡲ࡯ࡳࡦࡪࠧ୶")
bstack111ll_opy_ = [bstack1l1_opy_ (u"ࠩ࠱ࡥࡵࡱࠧ୷"), bstack1l1_opy_ (u"ࠪ࠲ࡦࡧࡢࠨ୸"), bstack1l1_opy_ (u"ࠫ࠳࡯ࡰࡢࠩ୹")]
bstack1lllll_opy_ = [bstack1l1_opy_ (u"ࠬ࡯ࡤࠨ୺"), bstack1l1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ୻"), bstack1l1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ୼"), bstack1l1_opy_ (u"ࠨࡵ࡫ࡥࡷ࡫ࡡࡣ࡮ࡨࡣ࡮ࡪࠧ୽")]
bstack1111_opy_ = {
  bstack1l1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୾"): bstack1l1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୿"),
  bstack1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ஀"): bstack1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪ஁"),
  bstack1l1_opy_ (u"࠭ࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫஂ"): bstack1l1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨஃ"),
  bstack1l1_opy_ (u"ࠨ࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ஄"): bstack1l1_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨஅ"),
  bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࡒࡴࡹ࡯࡯࡯ࡵࠪஆ"): bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬஇ")
}
bstack1lll1l_opy_ = [
  bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪஈ"),
  bstack1l1_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫஉ"),
  bstack1l1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨஊ"),
  bstack1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ஋"),
  bstack1l1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ஌"),
]
bstack1llll_opy_ = bstack1llll1_opy_ + bstack1ll1l_opy_ + bstack1lll11_opy_
bstack1lllll1l_opy_ = bstack1l1_opy_ (u"ࠪࡗࡪࡺࡴࡪࡰࡪࠤࡺࡶࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠯ࠤࡺࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡀࠠࡼࡿࠪ஍")
bstack111111_opy_ = bstack1l1_opy_ (u"ࠫࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡴࡧࡷࡹࡵࠧࠧஎ")
bstack111ll1l1_opy_ = bstack1l1_opy_ (u"ࠬࡖࡡࡳࡵࡨࡨࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧஏ")
bstack1l11l11_opy_ = bstack1l1_opy_ (u"࠭ࡓࡢࡰ࡬ࡸ࡮ࢀࡥࡥࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫஐ")
bstack11lll1l_opy_ = bstack1l1_opy_ (u"ࠧࡖࡵ࡬ࡲ࡬ࠦࡨࡶࡤࠣࡹࡷࡲ࠺ࠡࡽࢀࠫ஑")
bstack1lllll1ll_opy_ = bstack1l1_opy_ (u"ࠨࡕࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥࢁࡽࠨஒ")
bstack1111l1ll_opy_ = bstack1l1_opy_ (u"ࠩࡕࡩࡨ࡫ࡩࡷࡧࡧࠤ࡮ࡴࡴࡦࡴࡵࡹࡵࡺࠬࠡࡧࡻ࡭ࡹ࡯࡮ࡨࠩஓ")
bstack1111111l_opy_ = bstack1l1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷ࠳ࠦࡠࡱ࡫ࡳࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡠࠨஔ")
bstack1lll11l1_opy_ = bstack1l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸࠥࡧ࡮ࡥࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡶࡩࡱ࡫࡮ࡪࡷࡰࠤࡵࡧࡣ࡬ࡣࡪࡩࡸ࠴ࠠࡡࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹࠦࡰࡺࡶࡨࡷࡹ࠳ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡡࠩக")
bstack1l1ll1l1_opy_ = bstack1l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡲࡰࡤࡲࡸ࠱ࠦࡰࡢࡤࡲࡸࠥࡧ࡮ࡥࠢࡶࡩࡱ࡫࡮ࡪࡷࡰࡰ࡮ࡨࡲࡢࡴࡼࠤࡵࡧࡣ࡬ࡣࡪࡩࡸࠦࡴࡰࠢࡵࡹࡳࠦࡲࡰࡤࡲࡸࠥࡺࡥࡴࡶࡶࠤ࡮ࡴࠠࡱࡣࡵࡥࡱࡲࡥ࡭࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡵࡳࡧࡵࡴࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣࡶࡴࡨ࡯ࡵࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠱ࡵࡧࡢࡰࡶࠣࡶࡴࡨ࡯ࡵࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠱ࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡲࡩࡣࡴࡤࡶࡾࡦࠧ஖")
bstack1ll1ll1l_opy_ = bstack1l1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡵࡱࠣࡶࡺࡴࠠࡵࡧࡶࡸࡸ࠴ࠠࡡࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡢࡦࡪࡤࡺࡪࡦࠧ஗")
bstack1l1l11_opy_ = bstack1l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡣࡳࡴ࡮ࡻ࡭࠮ࡥ࡯࡭ࡪࡴࡴࠡࡶࡲࠤࡷࡻ࡮ࠡࡶࡨࡷࡹࡹ࠮ࠡࡢࡳ࡭ࡵࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡂࡲࡳ࡭ࡺࡳ࠭ࡑࡻࡷ࡬ࡴࡴ࠭ࡄ࡮࡬ࡩࡳࡺࡠࠨ஘")
bstack1lll11l_opy_ = bstack1l1_opy_ (u"ࠨࡊࡤࡲࡩࡲࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡲ࡯ࡴࡧࠪங")
bstack1l1ll11_opy_ = bstack1l1_opy_ (u"ࠩࡄࡰࡱࠦࡤࡰࡰࡨࠥࠬச")
bstack1l1l11l1_opy_ = bstack1l1_opy_ (u"ࠪࡇࡴࡴࡦࡪࡩࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵࠢࡤࡸࠥࠨࡻࡾࠤ࠱ࠤࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡣ࡭ࡷࡧࡩࠥࡧࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠣࡪ࡮ࡲࡥࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡪࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࡹ࠮ࠨ஛")
bstack111111l1_opy_ = bstack1l1_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡷ࡫ࡤࡦࡰࡷ࡭ࡦࡲࡳࠡࡰࡲࡸࠥࡶࡲࡰࡸ࡬ࡨࡪࡪ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡣࡧࡨࠥࡺࡨࡦ࡯ࠣ࡭ࡳࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡢࡵࠣࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨࠠࡢࡰࡧࠤࠧࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠣࠢࡲࡶࠥࡹࡥࡵࠢࡷ࡬ࡪࡳࠠࡢࡵࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴࠡࡸࡤࡶ࡮ࡧࡢ࡭ࡧࡶ࠾ࠥࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢࠡࡣࡱࡨࠥࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠤࠪஜ")
bstack111l111l_opy_ = bstack1l1_opy_ (u"ࠬࡓࡡ࡭ࡨࡲࡶࡲ࡫ࡤࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࡀࠢࡼࡿࠥࠫ஝")
bstack1llllllll_opy_ = bstack1l1_opy_ (u"࠭ࡅ࡯ࡥࡲࡹࡳࡺࡥࡳࡧࡧࠤࡪࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡹࡵࠦ࠭ࠡࡽࢀࠫஞ")
bstack1llll1l1l_opy_ = bstack1l1_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠧட")
bstack1ll1l1l_opy_ = bstack1l1_opy_ (u"ࠨࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡏࡳࡨࡧ࡬ࠨ஠")
bstack1ll11111_opy_ = bstack1l1_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠠࡪࡵࠣࡲࡴࡽࠠࡳࡷࡱࡲ࡮ࡴࡧࠢࠩ஡")
bstack1l1lll_opy_ = bstack1l1_opy_ (u"ࠪࡇࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡳࡵࡣࡵࡸࠥࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡑࡵࡣࡢ࡮࠽ࠤࢀࢃࠧ஢")
bstack1llllll1l_opy_ = bstack1l1_opy_ (u"ࠫࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦ࡬ࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡽࡩࡵࡪࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࢁࡽࠨண")
bstack1ll1111l_opy_ = bstack1l1_opy_ (u"࡛ࠬࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡦࡨࡸࡦ࡯࡬ࡴ࠼ࠣࡿࢂ࠭த")
bstack1ll111_opy_ = bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴࠢࡾࢁࠬ஥")
bstack1llll1l1_opy_ = bstack1l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡱࡴࡲࡺ࡮ࡪࡥࠡࡣࡱࠤࡦࡶࡰࡳࡱࡳࡶ࡮ࡧࡴࡦࠢࡉ࡛ࠥ࠮ࡲࡰࡤࡲࡸ࠴ࡶࡡࡣࡱࡷ࠭ࠥ࡯࡮ࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪ࠲ࠠࡴ࡭࡬ࡴࠥࡺࡨࡦࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠥࡱࡥࡺࠢ࡬ࡲࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡯ࡦࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡶ࡭ࡲࡶ࡬ࡦࠢࡳࡽࡹ࡮࡯࡯ࠢࡶࡧࡷ࡯ࡰࡵࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡥࡳࡿࠠࡇ࡙࠱ࠫ஦")
bstack1lll1l111_opy_ = bstack1l1_opy_ (u"ࠨࡕࡨࡸࡹ࡯࡮ࡨࠢ࡫ࡸࡹࡶࡐࡳࡱࡻࡽ࠴࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥࡵ࡮ࠡࡥࡸࡶࡷ࡫࡮ࡵ࡮ࡼࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡱࡩࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࠨࡼࡿࠬ࠰ࠥࡶ࡬ࡦࡣࡶࡩࠥࡻࡰࡨࡴࡤࡨࡪࠦࡴࡰࠢࡖࡩࡱ࡫࡮ࡪࡷࡰࡂࡂ࠺࠮࠱࠰࠳ࠤࡴࡸࠠࡳࡧࡩࡩࡷࠦࡴࡰࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡻࡼࡽ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡴࡩࡳ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡲࡥ࡯࡫ࡸࡱ࠴ࡸࡵ࡯࠯ࡷࡩࡸࡺࡳ࠮ࡤࡨ࡬࡮ࡴࡤ࠮ࡲࡵࡳࡽࡿࠣࡱࡻࡷ࡬ࡴࡴࠠࡧࡱࡵࠤࡦࠦࡷࡰࡴ࡮ࡥࡷࡵࡵ࡯ࡦ࠱ࠫ஧")
bstack111ll111_opy_ = bstack1l1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡿ࡭࡭ࠢࡩ࡭ࡱ࡫࠮࠯ࠩந")
bstack1l111l11_opy_ = bstack1l1_opy_ (u"ࠪࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡺࡨࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠡࠨன")
bstack11l1ll11_opy_ = bstack1l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡷ࡬ࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧ࠱ࠤࢀࢃࠧப")
bstack1111l111_opy_ = bstack1l1_opy_ (u"ࠬࡋࡸࡱࡧࡦࡸࡪࡪࠠࡢࡶࠣࡰࡪࡧࡳࡵࠢ࠴ࠤ࡮ࡴࡰࡶࡶ࠯ࠤࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦ࠰ࠨ஫")
bstack1lllll1_opy_ = bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡪࡵࡳ࡫ࡱ࡫ࠥࡇࡰࡱࠢࡸࡴࡱࡵࡡࡥ࠰ࠣࡿࢂ࠭஬")
bstack1l11ll_opy_ = bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡲ࡯ࡢࡦࠣࡅࡵࡶ࠮ࠡࡋࡱࡺࡦࡲࡩࡥࠢࡩ࡭ࡱ࡫ࠠࡱࡣࡷ࡬ࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡼࡿ࠱ࠫ஭")
bstack1ll11l1_opy_ = bstack1l1_opy_ (u"ࠨࡍࡨࡽࡸࠦࡣࡢࡰࡱࡳࡹࠦࡣࡰ࠯ࡨࡼ࡮ࡹࡴࠡࡣࡶࠤࡦࡶࡰࠡࡸࡤࡰࡺ࡫ࡳ࠭ࠢࡸࡷࡪࠦࡡ࡯ࡻࠣࡳࡳ࡫ࠠࡱࡴࡲࡴࡪࡸࡴࡺࠢࡩࡶࡴࡳࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠱ࠦ࡯࡯࡮ࡼࠤࠧࡶࡡࡵࡪࠥࠤࡦࡴࡤࠡࠤࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠧࠦࡣࡢࡰࠣࡧࡴ࠳ࡥࡹ࡫ࡶࡸࠥࡺ࡯ࡨࡧࡷ࡬ࡪࡸ࠮ࠨம")
bstack1111lll_opy_ = bstack1l1_opy_ (u"ࠩ࡞ࡍࡳࡼࡡ࡭࡫ࡧࠤࡦࡶࡰࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࡠࠤࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠤࡦࡸࡥࠡࡽ࡬ࡨࡁࡹࡴࡳ࡫ࡱ࡫ࡃ࠲ࠠࡱࡣࡷ࡬ࡁࡹࡴࡳ࡫ࡱ࡫ࡃ࠲ࠠࡤࡷࡶࡸࡴࡳ࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡹࡨࡢࡴࡨࡥࡧࡲࡥࡠ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂࢂ࠴ࠠࡇࡱࡵࠤࡲࡵࡲࡦࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡴࡱ࡫ࡡࡴࡧࠣࡺ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡻࡼࡽ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡴࡩࡳ࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲࡳ࡭ࡺࡳ࠯ࡴࡧࡷ࠱ࡺࡶ࠭ࡵࡧࡶࡸࡸ࠵ࡳࡱࡧࡦ࡭࡫ࡿ࠭ࡢࡲࡳࠫய")
bstack11l1ll1l_opy_ = bstack1l1_opy_ (u"ࠪ࡟ࡎࡴࡶࡢ࡮࡬ࡨࠥࡧࡰࡱࠢࡳࡶࡴࡶࡥࡳࡶࡼࡡ࡙ࠥࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡸࡤࡰࡺ࡫ࡳࠡࡱࡩࠤࡦࡶࡰࠡࡣࡵࡩࠥࡵࡦࠡࡽ࡬ࡨࡁࡹࡴࡳ࡫ࡱ࡫ࡃ࠲ࠠࡱࡣࡷ࡬ࡁࡹࡴࡳ࡫ࡱ࡫ࡃ࠲ࠠࡤࡷࡶࡸࡴࡳ࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡹࡨࡢࡴࡨࡥࡧࡲࡥࡠ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂࢂ࠴ࠠࡇࡱࡵࠤࡲࡵࡲࡦࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡴࡱ࡫ࡡࡴࡧࠣࡺ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡻࡼࡽ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡨࡴࡩࡳ࠰ࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲࡳ࡭ࡺࡳ࠯ࡴࡧࡷ࠱ࡺࡶ࠭ࡵࡧࡶࡸࡸ࠵ࡳࡱࡧࡦ࡭࡫ࡿ࠭ࡢࡲࡳࠫர")
bstack1l1l111l_opy_ = bstack1l1_opy_ (u"࡚ࠫࡹࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡧࡰࡱࠢ࡬ࡨࠥࢁࡽࠡࡨࡲࡶࠥ࡮ࡡࡴࡪࠣ࠾ࠥࢁࡽ࠯ࠩற")
bstack11ll111_opy_ = bstack1l1_opy_ (u"ࠬࡇࡰࡱࠢࡘࡴࡱࡵࡡࡥࡧࡧࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻ࠱ࠤࡎࡊࠠ࠻ࠢࡾࢁࠬல")
bstack11l11111_opy_ = bstack1l1_opy_ (u"࠭ࡕࡴ࡫ࡱ࡫ࠥࡇࡰࡱࠢ࠽ࠤࢀࢃ࠮ࠨள")
bstack111l1l_opy_ = bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠠࡪࡵࠣࡲࡴࡺࠠࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡴࡸࠠࡷࡣࡱ࡭ࡱࡲࡡࠡࡲࡼࡸ࡭ࡵ࡮ࠡࡶࡨࡷࡹࡹࠬࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡱࡣࡵࡥࡱࡲࡥ࡭ࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲࠦ࠽ࠡ࠳ࠪழ")
bstack11l1l1l_opy_ = bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࠺ࠡࡽࢀࠫவ")
bstack1lll111l1_opy_ = bstack1l1_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡩ࡬ࡰࡵࡨࠤࡧࡸ࡯ࡸࡵࡨࡶ࠿ࠦࡻࡾࠩஶ")
bstack11l11ll1_opy_ = bstack1l1_opy_ (u"ࠪࡇࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡧࡦࡶࠣࡶࡪࡧࡳࡰࡰࠣࡪࡴࡸࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡧࡤࡸࡺࡸࡥࠡࡨࡤ࡭ࡱࡻࡲࡦ࠰ࠣࡿࢂ࠭ஷ")
from ._version import __version__
bstack1l1l11l_opy_ = None
CONFIG = {}
bstack1l1111l_opy_ = None
bstack11l111ll_opy_ = None
bstack1111l1l1_opy_ = None
bstack1lll1ll11_opy_ = -1
bstack11l1l1ll_opy_ = DEFAULT_LOG_LEVEL
bstack1ll111l_opy_ = 1
bstack11lllll_opy_ = False
bstack1l1l1l11_opy_ = bstack1l1_opy_ (u"ࠫࠬஸ")
bstack1ll1llll_opy_ = bstack1l1_opy_ (u"ࠬ࠭ஹ")
bstack111llll_opy_ = False
bstack11llll1l_opy_ = None
bstack111l1l1_opy_ = None
bstack1ll1l1_opy_ = None
bstack111l1l11_opy_ = None
bstack11llll11_opy_ = None
bstack11l1l111_opy_ = None
bstack111l1lll_opy_ = None
bstack1lll1l11_opy_ = None
bstack1l11l11l_opy_ = None
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1l1ll_opy_,
                    format=bstack1l1_opy_ (u"࠭࡜࡯ࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫ஺"),
                    datefmt=bstack1l1_opy_ (u"ࠧࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ஻"))
def bstack11l11l_opy_():
  global CONFIG
  global bstack11l1l1ll_opy_
  if bstack1l1_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ஼") in CONFIG:
    bstack11l1l1ll_opy_ = bstack11l11_opy_[CONFIG[bstack1l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫ஽")]]
    logging.getLogger().setLevel(bstack11l1l1ll_opy_)
def bstack1ll1lll1_opy_():
  from bstack11lll1ll_opy_.version import version as bstack1111ll1_opy_
  return version.parse(bstack1111ll1_opy_)
def bstack1l1l1ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111ll11_opy_():
  fileName = bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ா")
  bstack1lllll1l1_opy_ = os.path.abspath(fileName)
  if not os.path.exists(bstack1lllll1l1_opy_):
    fileName = bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨி")
    bstack1lllll1l1_opy_ = os.path.abspath(fileName)
    if not os.path.exists(bstack1lllll1l1_opy_):
      bstack1lll1111_opy_(
        bstack1l1l11l1_opy_.format(os.getcwd()))
  with open(bstack1lllll1l1_opy_, bstack1l1_opy_ (u"ࠬࡸࠧீ")) as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      bstack1lll1111_opy_(bstack111l111l_opy_.format(str(exc)))
def bstack1l11111_opy_(config):
  bstack11111ll1_opy_ = bstack11ll1ll_opy_(config)
  for option in list(bstack11111ll1_opy_):
    if option.lower() in bstack1111l_opy_ and option != bstack1111l_opy_[option.lower()]:
      bstack11111ll1_opy_[bstack1111l_opy_[option.lower()]] = bstack11111ll1_opy_[option]
      del bstack11111ll1_opy_[option]
  return config
def bstack1l1llll1_opy_(config):
  bstack1ll1l11_opy_ = config.keys()
  for bstack1llll11l_opy_, bstack11lll11l_opy_ in bstack11ll1_opy_.items():
    if bstack11lll11l_opy_ in bstack1ll1l11_opy_:
      config[bstack1llll11l_opy_] = config[bstack11lll11l_opy_]
      del config[bstack11lll11l_opy_]
  for bstack1llll11l_opy_, bstack11lll11l_opy_ in bstack11111_opy_.items():
    for bstack11l111l_opy_ in bstack11lll11l_opy_:
      if bstack11l111l_opy_ in bstack1ll1l11_opy_:
        config[bstack1llll11l_opy_] = config[bstack11l111l_opy_]
        del config[bstack11l111l_opy_]
  for bstack11l111l_opy_ in list(config):
    for bstack1111l1_opy_ in bstack1llll_opy_:
      if bstack11l111l_opy_.lower() == bstack1111l1_opy_.lower() and bstack11l111l_opy_ != bstack1111l1_opy_:
        config[bstack1111l1_opy_] = config[bstack11l111l_opy_]
        del config[bstack11l111l_opy_]
  bstack1111lll1_opy_ = []
  if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩு") in config:
    bstack1111lll1_opy_ = config[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪூ")]
  for platform in bstack1111lll1_opy_:
    for bstack11l111l_opy_ in list(platform):
      for bstack1111l1_opy_ in bstack1llll_opy_:
        if bstack11l111l_opy_.lower() == bstack1111l1_opy_.lower() and bstack11l111l_opy_ != bstack1111l1_opy_:
          platform[bstack1111l1_opy_] = platform[bstack11l111l_opy_]
          del platform[bstack11l111l_opy_]
  for bstack1llll11l_opy_, bstack11lll11l_opy_ in bstack1l111_opy_.items():
    for platform in bstack1111lll1_opy_:
      if isinstance(bstack11lll11l_opy_, list):
        for bstack11l111l_opy_ in bstack11lll11l_opy_:
          if bstack11l111l_opy_ in platform:
            platform[bstack1llll11l_opy_] = platform[bstack11l111l_opy_]
            del platform[bstack11l111l_opy_]
            break
      elif bstack11lll11l_opy_ in platform:
        platform[bstack1llll11l_opy_] = platform[bstack11lll11l_opy_]
        del platform[bstack11lll11l_opy_]
  for bstack1l1111ll_opy_ in bstack1111_opy_:
    if bstack1l1111ll_opy_ in config:
      if not bstack1111_opy_[bstack1l1111ll_opy_] in config:
        config[bstack1111_opy_[bstack1l1111ll_opy_]] = {}
      config[bstack1111_opy_[bstack1l1111ll_opy_]].update(config[bstack1l1111ll_opy_])
      del config[bstack1l1111ll_opy_]
  for platform in bstack1111lll1_opy_:
    for bstack1l1111ll_opy_ in bstack1111_opy_:
      if bstack1l1111ll_opy_ in list(platform):
        if not bstack1111_opy_[bstack1l1111ll_opy_] in platform:
          platform[bstack1111_opy_[bstack1l1111ll_opy_]] = {}
        platform[bstack1111_opy_[bstack1l1111ll_opy_]].update(platform[bstack1l1111ll_opy_])
        del platform[bstack1l1111ll_opy_]
  config = bstack1l11111_opy_(config)
  return config
def bstack1l111ll_opy_(config):
  global bstack1ll1llll_opy_
  if bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ௃") in config and str(config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭௄")]).lower() != bstack1l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ௅"):
    if not bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨெ") in config:
      config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩே")] = {}
    if not bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨை") in config[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ௉")]:
      if bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪொ") in os.environ:
        config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ோ")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬௌ")] = os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ்࠭")]
      else:
        current_time = datetime.datetime.now()
        bstack1lllllll1_opy_ = current_time.strftime(bstack1l1_opy_ (u"ࠬࠫࡤࡠࠧࡥࡣࠪࡎࠥࡎࠩ௎"))
        hostname = socket.gethostname()
        bstack1l11111l_opy_ = bstack1l1_opy_ (u"࠭ࠧ௏").join(random.choices(string.ascii_lowercase + string.digits, k=4))
        identifier = bstack1l1_opy_ (u"ࠧࡼࡿࡢࡿࢂࡥࡻࡾࠩௐ").format(bstack1lllllll1_opy_, hostname, bstack1l11111l_opy_)
        config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ௑")][bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௒")] = identifier
    bstack1ll1llll_opy_ = config[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ௓")][bstack1l1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௔")]
  return config
def bstack11111l1_opy_(config):
  if bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ௕") in config and config[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ௖")] not in bstack11l1_opy_:
    return config[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪௗ")]
  elif bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ௘") in os.environ:
    return os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ௙")]
  else:
    return None
def bstack11l1ll_opy_(config):
  if bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊ࠭௚") in os.environ:
    return os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠧ௛")]
  elif bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௜") in config:
    return config[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௝")]
  else:
    return None
def bstack1l1l1l1l_opy_():
  if (
    isinstance(os.getenv(bstack1l1_opy_ (u"ࠧࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠬ௞")), str) and len(os.getenv(bstack1l1_opy_ (u"ࠨࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑ࠭௟"))) > 0
  ) or (
    isinstance(os.getenv(bstack1l1_opy_ (u"ࠩࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠨ௠")), str) and len(os.getenv(bstack1l1_opy_ (u"ࠪࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠩ௡"))) > 0
  ):
    return os.getenv(bstack1l1_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠪ௢"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠬࡉࡉࠨ௣"))).lower() == bstack1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫ௤") and str(os.getenv(bstack1l1_opy_ (u"ࠧࡄࡋࡕࡇࡑࡋࡃࡊࠩ௥"))).lower() == bstack1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭௦"):
    return os.getenv(bstack1l1_opy_ (u"ࠩࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠬ௧"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠪࡇࡎ࠭௨"))).lower() == bstack1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ௩") and str(os.getenv(bstack1l1_opy_ (u"࡚ࠬࡒࡂࡘࡌࡗࠬ௪"))).lower() == bstack1l1_opy_ (u"࠭ࡴࡳࡷࡨࠫ௫"):
    return os.getenv(bstack1l1_opy_ (u"ࠧࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭௬"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠨࡅࡌࠫ௭"))).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ௮") and str(os.getenv(bstack1l1_opy_ (u"ࠪࡇࡎࡥࡎࡂࡏࡈࠫ௯"))).lower() == bstack1l1_opy_ (u"ࠫࡨࡵࡤࡦࡵ࡫࡭ࡵ࠭௰"):
    return 0 # bstack1l1l111_opy_ bstack111lll11_opy_ not set build number env
  if os.getenv(bstack1l1_opy_ (u"ࠬࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡕࡅࡓࡉࡈࠨ௱")) and os.getenv(bstack1l1_opy_ (u"࠭ࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡆࡓࡒࡓࡉࡕࠩ௲")):
    return os.getenv(bstack1l1_opy_ (u"ࠧࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠩ௳"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠨࡅࡌࠫ௴"))).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ௵") and str(os.getenv(bstack1l1_opy_ (u"ࠪࡈࡗࡕࡎࡆࠩ௶"))).lower() == bstack1l1_opy_ (u"ࠫࡹࡸࡵࡦࠩ௷"):
    return os.getenv(bstack1l1_opy_ (u"ࠬࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠪ௸"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"࠭ࡃࡊࠩ௹"))).lower() == bstack1l1_opy_ (u"ࠧࡵࡴࡸࡩࠬ௺") and str(os.getenv(bstack1l1_opy_ (u"ࠨࡕࡈࡑࡆࡖࡈࡐࡔࡈࠫ௻"))).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ௼"):
    return os.getenv(bstack1l1_opy_ (u"ࠪࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉ࠭௽"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠫࡈࡏࠧ௾"))).lower() == bstack1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪ௿") and str(os.getenv(bstack1l1_opy_ (u"࠭ࡇࡊࡖࡏࡅࡇࡥࡃࡊࠩఀ"))).lower() == bstack1l1_opy_ (u"ࠧࡵࡴࡸࡩࠬఁ"):
    return os.getenv(bstack1l1_opy_ (u"ࠨࡅࡌࡣࡏࡕࡂࡠࡋࡇࠫం"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠩࡆࡍࠬః"))).lower() == bstack1l1_opy_ (u"ࠪࡸࡷࡻࡥࠨఄ") and str(os.getenv(bstack1l1_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠧఅ"))).lower() == bstack1l1_opy_ (u"ࠬࡺࡲࡶࡧࠪఆ"):
    return os.getenv(bstack1l1_opy_ (u"࠭ࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠨఇ"), 0)
  if str(os.getenv(bstack1l1_opy_ (u"ࠧࡕࡈࡢࡆ࡚ࡏࡌࡅࠩఈ"))).lower() == bstack1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ఉ"):
    return os.getenv(bstack1l1_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩఊ"), 0)
  return -1
def bstack1l1l1lll_opy_(bstack1lll11ll1_opy_):
  global CONFIG
  if not bstack1l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬఋ") in CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ఌ")]:
    return
  CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ఍")] = CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨఎ")].replace(
    bstack1l1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩఏ"),
    str(bstack1lll11ll1_opy_)
  )
def bstack1l1111l1_opy_():
  global CONFIG
  if not bstack1l1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧఐ") in CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ఑")]:
    return
  current_time = datetime.datetime.now()
  bstack1lllllll1_opy_ = current_time.strftime(bstack1l1_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨఒ"))
  CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ఓ")] = CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧఔ")].replace(
    bstack1l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬక"),
    bstack1lllllll1_opy_
  )
def bstack11111lll_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩఖ") in CONFIG and not bool(CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪగ")]):
    del CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫఘ")]
    return
  if not bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬఙ") in CONFIG:
    CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭చ")] = bstack1l1_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨఛ")
  if bstack1l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬజ") in CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩఝ")]:
    bstack1l1111l1_opy_()
    os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬఞ")] = CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫట")]
  if not bstack1l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬఠ") in CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭డ")]:
    return
  bstack1lll11ll1_opy_ = bstack1l1_opy_ (u"ࠬ࠭ఢ")
  bstack1l111ll1_opy_ = bstack1l1l1l1l_opy_()
  if bstack1l111ll1_opy_ != -1:
    bstack1lll11ll1_opy_ = bstack1l1_opy_ (u"࠭ࡃࡊࠢࠪణ") + str(bstack1l111ll1_opy_)
  if bstack1lll11ll1_opy_ == bstack1l1_opy_ (u"ࠧࠨత"):
    bstack11l1111_opy_ = bstack111l11ll_opy_(CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫథ")])
    if bstack11l1111_opy_ != -1:
      bstack1lll11ll1_opy_ = str(bstack11l1111_opy_)
  if bstack1lll11ll1_opy_:
    bstack1l1l1lll_opy_(bstack1lll11ll1_opy_)
    os.environ[bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ద")] = CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬధ")]
def bstack111ll1_opy_(bstack1llll1ll1_opy_, bstack1l1ll11l_opy_, path):
  bstack11ll11l1_opy_ = {
    bstack1l1_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨన"): bstack1l1ll11l_opy_
  }
  if os.path.exists(path):
    bstack1111ll_opy_ = json.load(open(path, bstack1l1_opy_ (u"ࠬࡸࡢࠨ఩")))
  else:
    bstack1111ll_opy_ = {}
  bstack1111ll_opy_[bstack1llll1ll1_opy_] = bstack11ll11l1_opy_
  with open(path, bstack1l1_opy_ (u"ࠨࡷࠬࠤప")) as outfile:
    json.dump(bstack1111ll_opy_, outfile)
def bstack111l11ll_opy_(bstack1llll1ll1_opy_):
  bstack1llll1ll1_opy_ = str(bstack1llll1ll1_opy_)
  bstack1lll1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩఫ")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨబ"))
  try:
    if not os.path.exists(bstack1lll1l1_opy_):
      os.makedirs(bstack1lll1l1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫభ")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪమ"), bstack1l1_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭య"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1_opy_ (u"ࠬࡽࠧర")):
        pass
      with open(file_path, bstack1l1_opy_ (u"ࠨࡷࠬࠤఱ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1_opy_ (u"ࠧࡳࠩల")) as bstack1ll11l11_opy_:
      bstack11l1lll1_opy_ = json.load(bstack1ll11l11_opy_)
    if bstack1llll1ll1_opy_ in bstack11l1lll1_opy_:
      bstack1111ll1l_opy_ = bstack11l1lll1_opy_[bstack1llll1ll1_opy_][bstack1l1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬళ")]
      bstack1llll111l_opy_ = int(bstack1111ll1l_opy_) + 1
      bstack111ll1_opy_(bstack1llll1ll1_opy_, bstack1llll111l_opy_, file_path)
      return bstack1llll111l_opy_
    else:
      bstack111ll1_opy_(bstack1llll1ll1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11l1l1l_opy_.format(str(e)))
    return -1
def bstack1ll111l1_opy_(config):
  if bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫఴ") in config and config[bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬవ")] not in bstack1l11_opy_:
    return config[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭శ")]
  elif bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ష") in os.environ:
    return os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧస")]
  else:
    return None
def bstack1l11l1l1_opy_(config):
  if not bstack1ll111l1_opy_(config) or not bstack11111l1_opy_(config):
    return True
  else:
    return False
def bstack1ll1l1l1_opy_(config):
  if bstack1l1l1ll_opy_() < version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭హ")):
    return False
  if bstack1l1l1ll_opy_() >= version.parse(bstack1l1_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧ఺")):
    return True
  if bstack1l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ఻") in config and config[bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅ఼ࠪ")] == False:
    return False
  else:
    return True
def bstack1lllll11l_opy_(config, index = 0):
  global bstack111llll_opy_
  bstack11l11lll_opy_ = {}
  caps = bstack1llll1_opy_ + bstack1l11l_opy_
  if bstack111llll_opy_:
    caps += bstack1lll11_opy_
  for key in config:
    if key in caps + [bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧఽ")]:
      continue
    bstack11l11lll_opy_[key] = config[key]
  if bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨా") in config:
    for bstack11lll1l1_opy_ in config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩి")][index]:
      if bstack11lll1l1_opy_ in caps + [bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬీ"), bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩు")]:
        continue
      bstack11l11lll_opy_[bstack11lll1l1_opy_] = config[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬూ")][index][bstack11lll1l1_opy_]
  bstack11l11lll_opy_[bstack1l1_opy_ (u"ࠪ࡬ࡴࡹࡴࡏࡣࡰࡩࠬృ")] = socket.gethostname()
  return bstack11l11lll_opy_
def bstack1l1l1111_opy_(config):
  global bstack111llll_opy_
  bstack1ll1l11l_opy_ = {}
  caps = bstack1l11l_opy_
  if bstack111llll_opy_:
    caps+= bstack1lll11_opy_
  for key in caps:
    if key in config:
      bstack1ll1l11l_opy_[key] = config[key]
  return bstack1ll1l11l_opy_
def bstack1l1l1l1_opy_(bstack11l11lll_opy_, bstack1ll1l11l_opy_):
  bstack1l11lll1_opy_ = {}
  for key in bstack11l11lll_opy_.keys():
    if key in bstack11ll1_opy_:
      bstack1l11lll1_opy_[bstack11ll1_opy_[key]] = bstack11l11lll_opy_[key]
    else:
      bstack1l11lll1_opy_[key] = bstack11l11lll_opy_[key]
  for key in bstack1ll1l11l_opy_:
    if key in bstack11ll1_opy_:
      bstack1l11lll1_opy_[bstack11ll1_opy_[key]] = bstack1ll1l11l_opy_[key]
    else:
      bstack1l11lll1_opy_[key] = bstack1ll1l11l_opy_[key]
  return bstack1l11lll1_opy_
def bstack1l11ll1_opy_(config, index = 0):
  global bstack111llll_opy_
  caps = {}
  bstack1ll1l11l_opy_ = bstack1l1l1111_opy_(config)
  bstack1ll11l1l_opy_ = bstack1l11l_opy_
  bstack1ll11l1l_opy_ += bstack1lll1l_opy_
  if bstack111llll_opy_:
    bstack1ll11l1l_opy_ += bstack1lll11_opy_
  if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౄ") in config:
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ౅") in config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩె")][index]:
      caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬే")] = config[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫై")][index][bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ౉")]
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫొ") in config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧో")][index]:
      caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ౌ")] = str(config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ్ࠩ")][index][bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ౎")])
    bstack1lll11l1l_opy_ = {}
    for bstack11ll1l1l_opy_ in bstack1ll11l1l_opy_:
      if bstack11ll1l1l_opy_ in config[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ౏")][index]:
        if bstack11ll1l1l_opy_ == bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ౐"):
          bstack1lll11l1l_opy_[bstack11ll1l1l_opy_] = str(config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭౑")][index][bstack11ll1l1l_opy_] * 1.0)
        else:
          bstack1lll11l1l_opy_[bstack11ll1l1l_opy_] = config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ౒")][index][bstack11ll1l1l_opy_]
        del(config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౓")][index][bstack11ll1l1l_opy_])
    bstack1ll1l11l_opy_ = update(bstack1ll1l11l_opy_, bstack1lll11l1l_opy_)
  bstack11l11lll_opy_ = bstack1lllll11l_opy_(config, index)
  if bstack1ll1l1l1_opy_(config):
    bstack11l11lll_opy_[bstack1l1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭౔")] = True
    caps.update(bstack1ll1l11l_opy_)
    caps[bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨౕ")] = bstack11l11lll_opy_
  else:
    bstack11l11lll_opy_[bstack1l1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨౖ")] = False
    caps.update(bstack1l1l1l1_opy_(bstack11l11lll_opy_, bstack1ll1l11l_opy_))
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ౗") in caps:
      caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫౘ")] = caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩౙ")]
      del(caps[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪౚ")])
    if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ౛") in caps:
      caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ౜")] = caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩౝ")]
      del(caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౞")])
  return caps
def bstack1l11lll_opy_():
  if bstack1l1l1ll_opy_() <= version.parse(bstack1l1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ౟")):
    return bstack11l1l_opy_
  return bstack1l1l1_opy_
def bstack1l111lll_opy_(options):
  return hasattr(options, bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬౠ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] += v
      else:
        d[k] = v
  return d
def bstack1ll11l_opy_(options, bstack11l1lll_opy_):
  for bstack1l11ll11_opy_ in bstack11l1lll_opy_:
    if bstack1l11ll11_opy_ in [bstack1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪౡ"), bstack1l1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪౢ")]:
      next
    if bstack1l11ll11_opy_ in options._experimental_options:
      options._experimental_options[bstack1l11ll11_opy_]= update(options._experimental_options[bstack1l11ll11_opy_], bstack11l1lll_opy_[bstack1l11ll11_opy_])
    else:
      options.add_experimental_option(bstack1l11ll11_opy_, bstack11l1lll_opy_[bstack1l11ll11_opy_])
  if bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬౣ") in bstack11l1lll_opy_:
    for arg in bstack11l1lll_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭౤")]:
      options.add_argument(arg)
    del(bstack11l1lll_opy_[bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ౥")])
  if bstack1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ౦") in bstack11l1lll_opy_:
    for ext in bstack11l1lll_opy_[bstack1l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ౧")]:
      options.add_extension(ext)
    del(bstack11l1lll_opy_[bstack1l1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ౨")])
def bstack1l111l1_opy_(options, bstack1ll11ll1_opy_):
  if bstack1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ౩") in bstack1ll11ll1_opy_:
    for bstack1llll1l_opy_ in bstack1ll11ll1_opy_[bstack1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭౪")]:
      if bstack1llll1l_opy_ in options._preferences:
        options._preferences[bstack1llll1l_opy_] = update(options._preferences[bstack1llll1l_opy_], bstack1ll11ll1_opy_[bstack1l1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ౫")][bstack1llll1l_opy_])
      else:
        options.set_preference(bstack1llll1l_opy_, bstack1ll11ll1_opy_[bstack1l1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ౬")][bstack1llll1l_opy_])
  if bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ౭") in bstack1ll11ll1_opy_:
    for arg in bstack1ll11ll1_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩ౮")]:
      options.add_argument(arg)
def bstack1111ll11_opy_(options, bstack11ll111l_opy_):
  if bstack1l1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭౯") in bstack11ll111l_opy_:
    options.use_webview(bool(bstack11ll111l_opy_[bstack1l1_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧ౰")]))
  bstack1ll11l_opy_(options, bstack11ll111l_opy_)
def bstack1l11llll_opy_(options, bstack111l111_opy_):
  for bstack1l1lll1l_opy_ in bstack111l111_opy_:
    if bstack1l1lll1l_opy_ in [bstack1l1_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫ౱"), bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭౲")]:
      next
    options.set_capability(bstack1l1lll1l_opy_, bstack111l111_opy_[bstack1l1lll1l_opy_])
  if bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ౳") in bstack111l111_opy_:
    for arg in bstack111l111_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ౴")]:
      options.add_argument(arg)
  if bstack1l1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨ౵") in bstack111l111_opy_:
    options.use_technology_preview(bool(bstack111l111_opy_[bstack1l1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩ౶")]))
def bstack111lll_opy_(options, bstack1l11l1_opy_):
  for bstack1lll11ll_opy_ in bstack1l11l1_opy_:
    if bstack1lll11ll_opy_ in [bstack1l1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ౷"), bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬ౸")]:
      next
    options._options[bstack1lll11ll_opy_] = bstack1l11l1_opy_[bstack1lll11ll_opy_]
  if bstack1l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ౹") in bstack1l11l1_opy_:
    for bstack1llllll_opy_ in bstack1l11l1_opy_[bstack1l1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭౺")]:
      options.add_additional_option(
          bstack1llllll_opy_, bstack1l11l1_opy_[bstack1l1_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ౻")][bstack1llllll_opy_])
  if bstack1l1_opy_ (u"ࠫࡦࡸࡧࡴࠩ౼") in bstack1l11l1_opy_:
    for arg in bstack1l11l1_opy_[bstack1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪ౽")]:
      options.add_argument(arg)
def bstack11llllll_opy_(options, caps):
  if not hasattr(options, bstack1l1_opy_ (u"࠭ࡋࡆ࡛ࠪ౾")):
    return
  if options.KEY == bstack1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ౿") and options.KEY in caps:
    bstack1ll11l_opy_(options, caps[bstack1l1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ಀ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧಁ") and options.KEY in caps:
    bstack1l111l1_opy_(options, caps[bstack1l1_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨಂ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬಃ") and options.KEY in caps:
    bstack1l11llll_opy_(options, caps[bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭಄")])
  elif options.KEY == bstack1l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧಅ") and options.KEY in caps:
    bstack1111ll11_opy_(options, caps[bstack1l1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨಆ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧಇ") and options.KEY in caps:
    bstack111lll_opy_(options, caps[bstack1l1_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨಈ")])
def bstack1l1111_opy_(caps):
  global bstack111llll_opy_
  if bstack111llll_opy_:
    if bstack1ll1lll1_opy_() < version.parse(bstack1l1_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩಉ")):
      return None
    else:
      from bstack11lll1ll_opy_.options.common.base import bstack11ll11l_opy_
      options = bstack11ll11l_opy_().bstack11ll1ll1_opy_(caps)
      return options
  else:
    browser = bstack1l1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫಊ")
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪಋ") in caps:
      browser = caps[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫಌ")]
    elif bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ಍") in caps:
      browser = caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩಎ")]
    browser = str(browser).lower()
    if browser == bstack1l1_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩಏ") or browser == bstack1l1_opy_ (u"ࠪ࡭ࡵࡧࡤࠨಐ"):
      browser = bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ಑")
    if browser == bstack1l1_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭ಒ"):
      browser = bstack1l1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ಓ")
    if browser not in [bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧಔ"), bstack1l1_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ಕ"), bstack1l1_opy_ (u"ࠩ࡬ࡩࠬಖ"), bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪಗ"), bstack1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬಘ")]:
      return None
    try:
      package = bstack1l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧಙ").format(browser)
      name = bstack1l1_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧಚ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l111lll_opy_(options):
        return None
      for bstack11l111l_opy_ in caps.keys():
        options.set_capability(bstack11l111l_opy_, caps[bstack11l111l_opy_])
      bstack11llllll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11ll1l_opy_(options, bstack1llll11_opy_):
  if not bstack1l111lll_opy_(options):
    return
  for bstack11l111l_opy_ in bstack1llll11_opy_.keys():
    if bstack11l111l_opy_ in bstack1lll1l_opy_:
      next
    if bstack11l111l_opy_ in options._caps and type(options._caps[bstack11l111l_opy_]) in [dict, list]:
      options._caps[bstack11l111l_opy_] = update(options._caps[bstack11l111l_opy_], bstack1llll11_opy_[bstack11l111l_opy_])
    else:
      options.set_capability(bstack11l111l_opy_, bstack1llll11_opy_[bstack11l111l_opy_])
  bstack11llllll_opy_(options, bstack1llll11_opy_)
  if bstack1l1_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ಛ") in options._caps:
    if options._caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ಜ")] and options._caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧಝ")].lower() != bstack1l1_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫಞ"):
      del options._caps[bstack1l1_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪಟ")]
def bstack11l11l1l_opy_(proxy_config):
  if bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩಠ") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨಡ")] = proxy_config[bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫಢ")]
    del(proxy_config[bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬಣ")])
  if bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬತ") in proxy_config and proxy_config[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ಥ")].lower() != bstack1l1_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫದ"):
    proxy_config[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨಧ")] = bstack1l1_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭ನ")
  if bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ಩") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫಪ")] = bstack1l1_opy_ (u"ࠩࡳࡥࡨ࠭ಫ")
  return proxy_config
def bstack11ll1111_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩಬ") in config:
    return proxy
  config[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪಭ")] = bstack11l11l1l_opy_(config[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫಮ")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬಯ")])
  return proxy
def bstack111l11_opy_(self):
  global CONFIG
  global bstack1lll1l11_opy_
  if bstack1l1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪರ") in CONFIG and bstack1l11lll_opy_().startswith(bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩಱ")):
    return CONFIG[bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬಲ")]
  elif bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧಳ") in CONFIG and bstack1l11lll_opy_().startswith(bstack1l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭಴")):
    return CONFIG[bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩವ")]
  else:
    return bstack1lll1l11_opy_(self)
def bstack1lll1llll_opy_():
  if bstack1l1l1ll_opy_() < version.parse(bstack1l1_opy_ (u"࠭࠴࠯࠲࠱࠴ࠬಶ")):
    logger.warning(bstack1lll1l111_opy_.format(bstack1l1l1ll_opy_()))
    return
  global bstack1lll1l11_opy_
  from selenium.webdriver.remote.remote_connection import RemoteConnection
  bstack1lll1l11_opy_ = RemoteConnection._get_proxy_url
  RemoteConnection._get_proxy_url = bstack111l11_opy_
def bstack1l111l1l_opy_(config):
  if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಷ") in config:
    if str(config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಸ")]).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧಹ"):
      return True
    else:
      return False
  elif bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࠨ಺") in os.environ:
    if str(os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࠩ಻")]).lower() == bstack1l1_opy_ (u"ࠬࡺࡲࡶࡧ಼ࠪ"):
      return True
    else:
      return False
  else:
    return False
def bstack11ll1ll_opy_(config):
  if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪಽ") in config:
    return config[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫಾ")]
  if bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧಿ") in config:
    return config[bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨೀ")]
  return {}
def bstack11l11l1_opy_(caps):
  global bstack1ll1llll_opy_
  if bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫು") in caps:
    caps[bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬೂ")][bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫೃ")] = True
    if bstack1ll1llll_opy_:
      caps[bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧೄ")][bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ೅")] = bstack1ll1llll_opy_
  else:
    caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ೆ")] = True
    if bstack1ll1llll_opy_:
      caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪೇ")] = bstack1ll1llll_opy_
def bstack1llll11ll_opy_():
  global CONFIG
  if bstack1l111l1l_opy_(CONFIG):
    bstack11111ll1_opy_ = bstack11ll1ll_opy_(CONFIG)
    bstack11lllll1_opy_(bstack11111l1_opy_(CONFIG), bstack11111ll1_opy_)
def bstack11lllll1_opy_(key, bstack11111ll1_opy_):
  global bstack1l1l11l_opy_
  logger.info(bstack1llll1l1l_opy_)
  try:
    bstack1l1l11l_opy_ = Local()
    bstack1l11ll1l_opy_ = {bstack1l1_opy_ (u"ࠪ࡯ࡪࡿࠧೈ"): key}
    bstack1l11ll1l_opy_.update(bstack11111ll1_opy_)
    logger.debug(bstack1llllll1l_opy_.format(str(bstack1l11ll1l_opy_)))
    bstack1l1l11l_opy_.start(**bstack1l11ll1l_opy_)
    if bstack1l1l11l_opy_.isRunning():
      logger.info(bstack1ll11111_opy_)
  except Exception as e:
    bstack1lll1111_opy_(bstack1l1lll_opy_.format(str(e)))
def bstack11l111_opy_():
  global bstack1l1l11l_opy_
  if bstack1l1l11l_opy_.isRunning():
    logger.info(bstack1ll1l1l_opy_)
    bstack1l1l11l_opy_.stop()
  bstack1l1l11l_opy_ = None
def bstack1llll1ll_opy_():
  logger.info(bstack1lll11l_opy_)
  global bstack1l1l11l_opy_
  if bstack1l1l11l_opy_:
    bstack11l111_opy_()
  logger.info(bstack1l1ll11_opy_)
def bstack11ll1l1_opy_(self, *args):
  logger.error(bstack1111l1ll_opy_)
  bstack1llll1ll_opy_()
  sys.exit(1)
def bstack1lll1111_opy_(err):
  logger.critical(bstack1llllllll_opy_.format(str(err)))
  atexit.unregister(bstack1llll1ll_opy_)
  sys.exit(1)
def bstack1ll1111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  atexit.unregister(bstack1llll1ll_opy_)
  sys.exit(1)
def bstack111lll1l_opy_():
  global CONFIG
  CONFIG = bstack111ll11_opy_()
  CONFIG = bstack1l1llll1_opy_(CONFIG)
  CONFIG = bstack1l111ll_opy_(CONFIG)
  if bstack1l11l1l1_opy_(CONFIG):
    bstack1lll1111_opy_(bstack111111l1_opy_)
  CONFIG[bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭೉")] = bstack1ll111l1_opy_(CONFIG)
  CONFIG[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨೊ")] = bstack11111l1_opy_(CONFIG)
  if bstack11l1ll_opy_(CONFIG):
    CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩೋ")] = bstack11l1ll_opy_(CONFIG)
    if not os.getenv(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠪೌ")):
      if os.getenv(bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈ್ࠬ")):
        CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ೎")] = os.getenv(bstack1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ೏"))
      else:
        bstack11111lll_opy_()
    else:
      if bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭೐") in CONFIG:
        del(CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ೑")])
  bstack111ll11l_opy_()
  bstack1l111l_opy_()
  if bstack111llll_opy_:
    CONFIG[bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ೒")] = bstack1l1lllll_opy_(CONFIG)
    logger.info(bstack11l11111_opy_.format(CONFIG[bstack1l1_opy_ (u"ࠧࡢࡲࡳࠫ೓")]))
def bstack1l111l_opy_():
  global CONFIG
  global bstack111llll_opy_
  if bstack1l1_opy_ (u"ࠨࡣࡳࡴࠬ೔") in CONFIG:
    try:
      from bstack11lll1ll_opy_ import version
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1l1l11_opy_)
    bstack111llll_opy_ = True
def bstack1l1lllll_opy_(config):
  bstack1ll1ll11_opy_ = bstack1l1_opy_ (u"ࠩࠪೕ")
  app = config[bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧೖ")]
  if isinstance(config[bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨ೗")], str):
    if os.path.splitext(app)[1] in bstack111ll_opy_:
      if os.path.exists(app):
        bstack1ll1ll11_opy_ = bstack1111l1l_opy_(config, app)
      elif bstack111l1l1l_opy_(app):
        bstack1ll1ll11_opy_ = app
      else:
        bstack1lll1111_opy_(bstack1l11ll_opy_.format(app))
    else:
      if bstack111l1l1l_opy_(app):
        bstack1ll1ll11_opy_ = app
      elif os.path.exists(app):
        bstack1ll1ll11_opy_ = bstack1111l1l_opy_(app)
      else:
        bstack1lll1111_opy_(bstack11l1ll1l_opy_)
  else:
    if len(app) > 2:
      bstack1lll1111_opy_(bstack1ll11l1_opy_)
    elif len(app) == 2:
      if bstack1l1_opy_ (u"ࠬࡶࡡࡵࡪࠪ೘") in app and bstack1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ೙") in app:
        if os.path.exists(app[bstack1l1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ೚")]):
          bstack1ll1ll11_opy_ = bstack1111l1l_opy_(config, app[bstack1l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭೛")], app[bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ೜")])
        else:
          bstack1lll1111_opy_(bstack1l11ll_opy_.format(app))
      else:
        bstack1lll1111_opy_(bstack1ll11l1_opy_)
    else:
      for key in app:
        if key in bstack1lllll_opy_:
          if key == bstack1l1_opy_ (u"ࠪࡴࡦࡺࡨࠨೝ"):
            if os.path.exists(app[key]):
              bstack1ll1ll11_opy_ = bstack1111l1l_opy_(config, app[key])
            else:
              bstack1lll1111_opy_(bstack1l11ll_opy_.format(app))
          else:
            bstack1ll1ll11_opy_ = app[key]
        else:
          bstack1lll1111_opy_(bstack1111lll_opy_)
  return bstack1ll1ll11_opy_
def bstack111l1l1l_opy_(bstack1ll1ll11_opy_):
  import re
  bstack1lllllll_opy_ = re.compile(bstack1l1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦೞ"))
  bstack11ll11ll_opy_ = re.compile(bstack1l1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ೟"))
  if bstack1l1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬೠ") in bstack1ll1ll11_opy_ or re.fullmatch(bstack1lllllll_opy_, bstack1ll1ll11_opy_) or re.fullmatch(bstack11ll11ll_opy_, bstack1ll1ll11_opy_):
    return True
  else:
    return False
def bstack1111l1l_opy_(config, path, bstack1lll1ll1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1_opy_ (u"ࠧࡳࡤࠪೡ")).read()).hexdigest()
  bstack111l1111_opy_ = bstack1l11l1ll_opy_(md5_hash)
  bstack1ll1ll11_opy_ = None
  if bstack111l1111_opy_:
    logger.info(bstack1l1l111l_opy_.format(bstack111l1111_opy_, md5_hash))
    return bstack111l1111_opy_
  bstack11l11ll_opy_ = MultipartEncoder(
    fields={
        bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ೢ"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1_opy_ (u"ࠩࡵࡦࠬೣ")), bstack1l1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ೤")),
        bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ೥"): bstack1lll1ll1_opy_
    }
  )
  response = requests.post(bstack1l1ll_opy_, data=bstack11l11ll_opy_,
                         headers={bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ೦"): bstack11l11ll_opy_.content_type}, auth=(bstack1ll111l1_opy_(config), bstack11111l1_opy_(config)))
  try:
    res = json.loads(response.text)
    bstack1ll1ll11_opy_ = res[bstack1l1_opy_ (u"࠭ࡡࡱࡲࡢࡹࡷࡲࠧ೧")]
    logger.info(bstack11ll111_opy_.format(bstack1ll1ll11_opy_))
    bstack1l111111_opy_(md5_hash, bstack1ll1ll11_opy_)
  except ValueError as err:
    bstack1lll1111_opy_(bstack1lllll1_opy_.format(str(err)))
  return bstack1ll1ll11_opy_
def bstack111ll11l_opy_():
  global CONFIG
  global bstack1ll111l_opy_
  bstack1ll11ll_opy_ = 1
  if bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ೨") in CONFIG:
    bstack1ll11ll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ೩")]
  bstack1111l11l_opy_ = 0
  if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ೪") in CONFIG:
    bstack1111l11l_opy_ = len(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೫")])
  bstack1ll111l_opy_ = int(bstack1ll11ll_opy_) * int(bstack1111l11l_opy_)
def bstack1l11l1ll_opy_(md5_hash):
  bstack1ll1l1ll_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠫࢃ࠭೬")), bstack1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ೭"), bstack1l1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ೮"))
  if os.path.exists(bstack1ll1l1ll_opy_):
    bstack1l1llll_opy_ = json.load(open(bstack1ll1l1ll_opy_,bstack1l1_opy_ (u"ࠧࡳࡤࠪ೯")))
    if md5_hash in bstack1l1llll_opy_:
      bstack11llll_opy_ = bstack1l1llll_opy_[md5_hash]
      bstack1lll11lll_opy_ = datetime.datetime.now()
      bstack1l1lll1_opy_ = datetime.datetime.strptime(bstack11llll_opy_[bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ೰")], bstack1l1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ೱ"))
      if (bstack1lll11lll_opy_ - bstack1l1lll1_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack11llll_opy_[bstack1l1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨೲ")]):
        return None
      return bstack11llll_opy_[bstack1l1_opy_ (u"ࠫ࡮ࡪࠧೳ")]
  else:
    return None
def bstack1l111111_opy_(md5_hash, bstack1ll1ll11_opy_):
  bstack1lll1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠬࢄࠧ೴")), bstack1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭೵"))
  if not os.path.exists(bstack1lll1l1_opy_):
    os.makedirs(bstack1lll1l1_opy_)
  bstack1ll1l1ll_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩ೶")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ೷"), bstack1l1_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ೸"))
  bstack1llllll11_opy_ = {
    bstack1l1_opy_ (u"ࠪ࡭ࡩ࠭೹"): bstack1ll1ll11_opy_,
    bstack1l1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ೺"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ೻")),
    bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ೼"): str(__version__)
  }
  if os.path.exists(bstack1ll1l1ll_opy_):
    bstack1l1llll_opy_ = json.load(open(bstack1ll1l1ll_opy_,bstack1l1_opy_ (u"ࠧࡳࡤࠪ೽")))
  else:
    bstack1l1llll_opy_ = {}
  bstack1l1llll_opy_[md5_hash] = bstack1llllll11_opy_
  with open(bstack1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠣࡹ࠮ࠦ೾")) as outfile:
    json.dump(bstack1l1llll_opy_, outfile)
def bstack1lll1ll1l_opy_(self):
  return
def bstack1111l11_opy_(self):
  return
def bstack1lll111ll_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1ll111ll_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1l1111l_opy_
  global bstack1lll1ll11_opy_
  global bstack1111l1l1_opy_
  global bstack11lllll_opy_
  global bstack1l1l1l11_opy_
  global bstack11llll1l_opy_
  CONFIG[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ೿")] = str(bstack1l1l1l11_opy_) + str(__version__)
  command_executor = bstack1l11lll_opy_()
  logger.debug(bstack11lll1l_opy_.format(command_executor))
  proxy = bstack11ll1111_opy_(CONFIG, proxy)
  bstack1l1ll1ll_opy_ = 0 if bstack1lll1ll11_opy_ < 0 else bstack1lll1ll11_opy_
  if bstack11lllll_opy_ is True:
    bstack1l1ll1ll_opy_ = int(threading.current_thread().getName())
  bstack1llll11_opy_ = bstack1l11ll1_opy_(CONFIG, bstack1l1ll1ll_opy_)
  logger.debug(bstack111ll1l1_opy_.format(str(bstack1llll11_opy_)))
  if bstack1l111l1l_opy_(CONFIG):
    bstack11l11l1_opy_(bstack1llll11_opy_)
  if desired_capabilities:
    if bstack1l1l1ll_opy_() < version.parse(bstack1l1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩഀ")):
      desired_capabilities.update(bstack1llll11_opy_)
    bstack11l111l1_opy_ = bstack1l11ll1_opy_(bstack1l1llll1_opy_(desired_capabilities))
    if bstack11l111l1_opy_:
      bstack1llll11_opy_ = update(bstack11l111l1_opy_, bstack1llll11_opy_)
  if options:
    bstack11ll1l_opy_(options, bstack1llll11_opy_)
  if not options:
    options = bstack1l1111_opy_(bstack1llll11_opy_)
  if options and bstack1l1l1ll_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪഁ")):
    desired_capabilities = None
  if (
      not options and not desired_capabilities
  ) or (
      bstack1l1l1ll_opy_() < version.parse(bstack1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫം")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llll11_opy_)
  logger.info(bstack111111_opy_)
  if bstack1l1l1ll_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬഃ")):
    bstack11llll1l_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l1ll_opy_() >= version.parse(bstack1l1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧഄ")):
    bstack11llll1l_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11llll1l_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  bstack1l1111l_opy_ = self.session_id
  if bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫഅ") in CONFIG and bstack1l1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧആ") in CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ഇ")][bstack1l1ll1ll_opy_]:
    bstack1111l1l1_opy_ = CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧഈ")][bstack1l1ll1ll_opy_][bstack1l1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪഉ")]
  logger.debug(bstack1lllll1ll_opy_.format(bstack1l1111l_opy_))
def bstack1ll1ll_opy_(self, test):
  global CONFIG
  global bstack1l1111l_opy_
  global bstack11l111ll_opy_
  global bstack1111l1l1_opy_
  global bstack111l1l1_opy_
  if bstack1l1111l_opy_:
    try:
      data = {}
      bstack111l1ll1_opy_ = None
      if test:
        bstack111l1ll1_opy_ = str(test.data)
      if bstack111l1ll1_opy_ and not bstack1111l1l1_opy_:
        data[bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫഊ")] = bstack111l1ll1_opy_
      if bstack11l111ll_opy_:
        if bstack11l111ll_opy_.status == bstack1l1_opy_ (u"ࠧࡑࡃࡖࡗࠬഋ"):
          data[bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨഌ")] = bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ഍")
        elif bstack11l111ll_opy_.status == bstack1l1_opy_ (u"ࠪࡊࡆࡏࡌࠨഎ"):
          data[bstack1l1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഏ")] = bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഐ")
          if bstack11l111ll_opy_.message:
            data[bstack1l1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭഑")] = str(bstack11l111ll_opy_.message)
      user = CONFIG[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩഒ")]
      key = CONFIG[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫഓ")]
      url = bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠵ࡻࡾ࠰࡭ࡷࡴࡴࠧഔ").format(user, key, bstack1l1111l_opy_)
      headers = {
        bstack1l1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩക"): bstack1l1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഖ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll111_opy_.format(str(e)))
  bstack111l1l1_opy_(self, test)
def bstack1lll1lll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll1l1_opy_
  bstack1ll1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l111ll_opy_
  bstack11l111ll_opy_ = self._test
def bstack1l1ll1_opy_(outs_dir, options, tests_root_name, stats, copied_artifacts, outputfile=None):
  from pabot import pabot
  outputfile = outputfile or options.get(bstack1l1_opy_ (u"ࠧࡵࡵࡵࡲࡸࡸࠧഗ"), bstack1l1_opy_ (u"ࠨ࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠥഘ"))
  output_path = os.path.abspath(
    os.path.join(options.get(bstack1l1_opy_ (u"ࠢࡰࡷࡷࡴࡺࡺࡤࡪࡴࠥങ"), bstack1l1_opy_ (u"ࠣ࠰ࠥച")), outputfile)
  )
  files = sorted(pabot.glob(os.path.join(pabot._glob_escape(outs_dir), bstack1l1_opy_ (u"ࠤ࠭࠲ࡽࡳ࡬ࠣഛ"))))
  if not files:
    pabot._write(bstack1l1_opy_ (u"࡛ࠪࡆࡘࡎ࠻ࠢࡑࡳࠥࡵࡵࡵࡲࡸࡸࠥ࡬ࡩ࡭ࡧࡶࠤ࡮ࡴࠠࠣࠧࡶࠦࠬജ") % outs_dir, pabot.Color.YELLOW)
    return bstack1l1_opy_ (u"ࠦࠧഝ")
  def invalid_xml_callback():
    global _ABNORMAL_EXIT_HAPPENED
    _ABNORMAL_EXIT_HAPPENED = True
  resu = pabot.merge(
    files, options, tests_root_name, copied_artifacts, invalid_xml_callback
  )
  pabot._update_stats(resu, stats)
  resu.save(output_path)
  return output_path
def bstack11l11l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  from pabot import pabot
  from robot import __version__ as ROBOT_VERSION
  from robot import rebot
  if bstack1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤഞ") in options:
    del options[bstack1l1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥട")]
  if ROBOT_VERSION < bstack1l1_opy_ (u"ࠢ࠵࠰࠳ࠦഠ"):
    stats = {
      bstack1l1_opy_ (u"ࠣࡥࡵ࡭ࡹ࡯ࡣࡢ࡮ࠥഡ"): {bstack1l1_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࠣഢ"): 0, bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥണ"): 0, bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦത"): 0},
      bstack1l1_opy_ (u"ࠧࡧ࡬࡭ࠤഥ"): {bstack1l1_opy_ (u"ࠨࡴࡰࡶࡤࡰࠧദ"): 0, bstack1l1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢധ"): 0, bstack1l1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣന"): 0},
    }
  else:
    stats = {
      bstack1l1_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࠣഩ"): 0,
      bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥപ"): 0,
      bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦഫ"): 0,
      bstack1l1_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠨബ"): 0,
    }
  if pabot_args[bstack1l1_opy_ (u"ࠨࡂࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡠࡔࡘࡒࠧഭ")]:
    outputs = []
    for index, _ in enumerate(pabot_args[bstack1l1_opy_ (u"ࠢࡃࡕࡗࡅࡈࡑ࡟ࡑࡃࡕࡅࡑࡒࡅࡍࡡࡕ࡙ࡓࠨമ")]):
      copied_artifacts = pabot._copy_output_artifacts(
        options, pabot_args[bstack1l1_opy_ (u"ࠣࡣࡵࡸ࡮࡬ࡡࡤࡶࡶࠦയ")], pabot_args[bstack1l1_opy_ (u"ࠤࡤࡶࡹ࡯ࡦࡢࡥࡷࡷ࡮ࡴࡳࡶࡤࡩࡳࡱࡪࡥࡳࡵࠥര")]
      )
      outputs += [
        bstack1l1ll1_opy_(
          os.path.join(outs_dir, str(index)+ bstack1l1_opy_ (u"ࠥ࠳ࠧറ")),
          options,
          tests_root_name,
          stats,
          copied_artifacts,
          outputfile=os.path.join(bstack1l1_opy_ (u"ࠦࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠦല"), bstack1l1_opy_ (u"ࠧࡵࡵࡵࡲࡸࡸࠪࡹ࠮ࡹ࡯࡯ࠦള") % index),
        )
      ]
    if bstack1l1_opy_ (u"ࠨ࡯ࡶࡶࡳࡹࡹࠨഴ") not in options:
      options[bstack1l1_opy_ (u"ࠢࡰࡷࡷࡴࡺࡺࠢവ")] = bstack1l1_opy_ (u"ࠣࡱࡸࡸࡵࡻࡴ࠯ࡺࡰࡰࠧശ")
    pabot._write_stats(stats)
    return rebot(*outputs, **pabot._options_for_rebot(options, start_time_string, pabot._now()))
  else:
    return pabot._report_results(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1lll1l1l_opy_(self, ff_profile_dir):
  global bstack111l1l11_opy_
  if not ff_profile_dir:
    return None
  return bstack111l1l11_opy_(self, ff_profile_dir)
def bstack11l1111l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll1llll_opy_
  bstack1lll1lll1_opy_ = []
  if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬഷ") in CONFIG:
    bstack1lll1lll1_opy_ = CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭സ")]
  bstack111lllll_opy_ = len(suite_group) * len(pabot_args[bstack1l1_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦഹ")] or [(bstack1l1_opy_ (u"ࠧࠨഺ"), None)]) * len(bstack1lll1lll1_opy_)
  pabot_args[bstack1l1_opy_ (u"ࠨࡂࡔࡖࡄࡇࡐࡥࡐࡂࡔࡄࡐࡑࡋࡌࡠࡔࡘࡒ഻ࠧ")] = []
  for q in range(bstack111lllll_opy_):
    pabot_args[bstack1l1_opy_ (u"ࠢࡃࡕࡗࡅࡈࡑ࡟ࡑࡃࡕࡅࡑࡒࡅࡍࡡࡕ࡙ࡓࠨ഼")].append(str(q))
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤഽ")],
      pabot_args[bstack1l1_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥാ")],
      argfile,
      pabot_args.get(bstack1l1_opy_ (u"ࠥ࡬࡮ࡼࡥࠣി")),
      pabot_args[bstack1l1_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢീ")],
      platform[0],
      bstack1ll1llll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧു")] or [(bstack1l1_opy_ (u"ࠨࠢൂ"), None)]
    for platform in enumerate(bstack1lll1lll1_opy_)
  ]
def bstack1111llll_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0,bstack11111l1l_opy_=bstack1l1_opy_ (u"ࠧࠨൃ")):
  global bstack11l1l111_opy_
  self.platform_index = platform_index
  self.bstack1llll11l1_opy_ = bstack11111l1l_opy_
  bstack11l1l111_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack1lll1ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111l1lll_opy_
  if not bstack1l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪൄ") in item.options:
    item.options[bstack1l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൅")] = []
  for v in item.options[bstack1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬെ")]:
    if bstack1l1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪേ") in v:
      item.options[bstack1l1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧൈ")].remove(v)
  item.options[bstack1l1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൉")].insert(0, bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾࠩൊ").format(item.platform_index))
  item.options[bstack1l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪോ")].insert(0, bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩൌ").format(item.bstack1llll11l1_opy_))
  return bstack111l1lll_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1lll11l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11llll11_opy_
  command[0] = command[0].replace(bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ്ࠩ"), bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨൎ"), 1)
  return bstack11llll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11ll1l11_opy_(self, runner, quiet=False, capture=True):
  global bstack1lll1l1ll_opy_
  bstack1l1ll1l_opy_ = bstack1lll1l1ll_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1l1_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ൏")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ൐")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1ll1l_opy_
def bstack11lll111_opy_(self, name, context, *args):
  global bstack11l1l11l_opy_
  if name in [bstack1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ൑"), bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪ൒")]:
    bstack11l1l11l_opy_(self, name, context, *args)
  if name == bstack1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠪ൓"):
    try:
      bstack1l11l1l_opy_ = str(self.feature.name)
      context.browser.execute_script(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨൔ") + json.dumps(bstack1l11l1l_opy_) + bstack1l1_opy_ (u"ࠫࢂࢃࠧൕ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬൖ").format(str(e)))
  if name == bstack1l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨൗ"):
    try:
      if not hasattr(self, bstack1l1_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ൘")):
        self.driver_before_scenario = True
      bstack111l11l1_opy_ = args[0].name
      bstack1llll111_opy_ = bstack1l11l1l_opy_ = str(self.feature.name)
      bstack1l11l1l_opy_ = bstack1llll111_opy_ + bstack1l1_opy_ (u"ࠨࠢ࠰ࠤࠬ൙") + bstack111l11l1_opy_
      if self.driver_before_scenario:
        context.browser.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ൚") + json.dumps(bstack1l11l1l_opy_) + bstack1l1_opy_ (u"ࠪࢁࢂ࠭൛"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ൜").format(str(e)))
  if name == bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭൝"):
    try:
      bstack1llll1111_opy_ = args[0].status.name
      if str(bstack1llll1111_opy_).lower() == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭൞"):
        bstack1ll1lll_opy_ = bstack1l1_opy_ (u"ࠧࠨൟ")
        bstack11l1l1l1_opy_ = bstack1l1_opy_ (u"ࠨࠩൠ")
        bstack1ll11lll_opy_ = bstack1l1_opy_ (u"ࠩࠪൡ")
        try:
          import traceback
          bstack1ll1lll_opy_ = self.exception.__class__.__name__
          bstack1l11l111_opy_ = traceback.format_tb(self.exc_traceback)
          bstack11l1l1l1_opy_ = bstack1l1_opy_ (u"ࠪࠤࠬൢ").join(bstack1l11l111_opy_)
          bstack1ll11lll_opy_ = bstack1l11l111_opy_[-1]
        except Exception as e:
          logger.debug(bstack11l11ll1_opy_.format(str(e)))
        bstack1ll1lll_opy_ += bstack1ll11lll_opy_
        context.browser.execute_script(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩൣ") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦ൤") + str(bstack11l1l1l1_opy_)) + bstack1l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭൥"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࠮ࠣࠦࡷ࡫ࡡࡴࡱࡱࠦ࠿ࠦࠧ൦") + json.dumps(bstack1l1_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ൧") + str(bstack1ll1lll_opy_)) + bstack1l1_opy_ (u"ࠩࢀࢁࠬ൨"))
      else:
        context.browser.execute_script(bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ൩") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣ൪")) + bstack1l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫ൫"))
        if self.driver_before_scenario:
          context.browser.execute_script(bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡹࡴࡢࡶࡸࡷࠧࡀࠢࡱࡣࡶࡷࡪࡪࠢࡾࡿࠪ൬"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ൭").format(str(e)))
  if name == bstack1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨ൮"):
    try:
      if context.failed is True:
        bstack11l1l11_opy_ = []
        bstack111lll1_opy_ = []
        bstack1lllll111_opy_ = []
        bstack11111111_opy_ = bstack1l1_opy_ (u"ࠩࠪ൯")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11l1l11_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l11l111_opy_ = traceback.format_tb(exc_tb)
            bstack11l1ll1_opy_ = bstack1l1_opy_ (u"ࠪࠤࠬ൰").join(bstack1l11l111_opy_)
            bstack111lll1_opy_.append(bstack11l1ll1_opy_)
            bstack1lllll111_opy_.append(bstack1l11l111_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l11ll1_opy_.format(str(e)))
        bstack1ll1lll_opy_ = bstack1l1_opy_ (u"ࠫࠬ൱")
        for i in range(len(bstack11l1l11_opy_)):
          bstack1ll1lll_opy_ += bstack11l1l11_opy_[i] + bstack1lllll111_opy_[i] + bstack1l1_opy_ (u"ࠬࡢ࡮ࠨ൲")
        bstack11111111_opy_ = bstack1l1_opy_ (u"࠭ࠠࠨ൳").join(bstack111lll1_opy_)
        if not self.driver_before_scenario:
          context.browser.execute_script(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ൴") + json.dumps(bstack11111111_opy_) + bstack1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ൵"))
          context.browser.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠥࡪࡦ࡯࡬ࡦࡦࠥ࠰ࠥࠨࡲࡦࡣࡶࡳࡳࠨ࠺ࠡࠩ൶") + json.dumps(bstack1l1_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣ൷") + str(bstack1ll1lll_opy_)) + bstack1l1_opy_ (u"ࠫࢂࢃࠧ൸"))
      else:
        if not self.driver_before_scenario:
          context.browser.execute_script(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ൹") + json.dumps(bstack1l1_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤൺ") + str(self.feature.name) + bstack1l1_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤൻ")) + bstack1l1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧർ"))
          context.browser.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠥࡴࡦࡹࡳࡦࡦࠥࢁࢂ࠭ൽ"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬൾ").format(str(e)))
  if name in [bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫൿ"), bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭඀")]:
    bstack11l1l11l_opy_(self, name, context, *args)
def bstack1lllll11_opy_(bstack11l1llll_opy_):
  global bstack1l1l1l11_opy_
  bstack1l1l1l11_opy_ = bstack11l1llll_opy_
  logger.info(bstack1lllll1l_opy_.format(bstack1l1l1l11_opy_.split(bstack1l1_opy_ (u"࠭࠭ࠨඁ"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack1ll1111_opy_(e, bstack1111111l_opy_)
  Service.start = bstack1lll1ll1l_opy_
  Service.stop = bstack1111l11_opy_
  webdriver.Remote.__init__ = bstack1ll111ll_opy_
  WebDriver.close = bstack1lll111ll_opy_
  if (bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ං") in str(bstack11l1llll_opy_).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1l1ll1l1_opy_)
    Output.end_test = bstack1ll1ll_opy_
    TestStatus.__init__ = bstack1lll1lll_opy_
    WebDriverCreator._get_ff_profile = bstack1lll1l1l_opy_
    QueueItem.__init__ = bstack1111llll_opy_
    pabot._create_items = bstack11l1111l_opy_
    pabot._run = bstack1lll11l11_opy_
    pabot._create_command_for_execution = bstack1lll1ll_opy_
    pabot._report_results = bstack11l11l11_opy_
  if bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨඃ") in str(bstack11l1llll_opy_).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1ll1ll1l_opy_)
    Runner.run_hook = bstack11lll111_opy_
    Step.run = bstack11ll1l11_opy_
def bstack1llll1lll_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ඄") in CONFIG and int(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪඅ")]) > 1:
    logger.warn(bstack111l1l_opy_)
def bstack1lll1l1l1_opy_(bstack111111l_opy_, index):
  bstack1lllll11_opy_(bstack1lll1_opy_)
  exec(open(bstack111111l_opy_).read())
def bstack11111l11_opy_(arg):
  global CONFIG
  bstack1lllll11_opy_(bstack111l1_opy_)
  os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬආ")] = CONFIG[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧඇ")]
  os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩඈ")] = CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪඉ")]
  from _pytest.config import main as bstack1l1lll11_opy_
  bstack1l1lll11_opy_(arg)
def bstack111111ll_opy_(arg):
  bstack1lllll11_opy_(bstack11lll_opy_)
  from behave.__main__ import main as bstack111l1ll_opy_
  bstack111l1ll_opy_(arg)
def bstack11lll1_opy_():
  logger.info(bstack111ll111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧඊ"), help=bstack1l1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩࠪඋ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠪ࠱ࡺ࠭ඌ"), bstack1l1_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨඍ"), help=bstack1l1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫඎ"))
  parser.add_argument(bstack1l1_opy_ (u"࠭࠭࡬ࠩඏ"), bstack1l1_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭ඐ"), help=bstack1l1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩඑ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠩ࠰ࡪࠬඒ"), bstack1l1_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨඓ"), help=bstack1l1_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪඔ"))
  bstack1llllll1_opy_ = parser.parse_args()
  try:
    bstack1lll111l_opy_ = bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩඕ")
    if bstack1llllll1_opy_.framework and bstack1llllll1_opy_.framework not in (bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඖ"), bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ඗")):
      bstack1lll111l_opy_ = bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧ඘")
    bstack111l11l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll111l_opy_)
    bstack11111ll_opy_ = open(bstack111l11l_opy_, bstack1l1_opy_ (u"ࠩࡵࠫ඙"))
    bstack11l1l1_opy_ = bstack11111ll_opy_.read()
    bstack11111ll_opy_.close()
    if bstack1llllll1_opy_.username:
      bstack11l1l1_opy_ = bstack11l1l1_opy_.replace(bstack1l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪක"), bstack1llllll1_opy_.username)
    if bstack1llllll1_opy_.key:
      bstack11l1l1_opy_ = bstack11l1l1_opy_.replace(bstack1l1_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ඛ"), bstack1llllll1_opy_.key)
    if bstack1llllll1_opy_.framework:
      bstack11l1l1_opy_ = bstack11l1l1_opy_.replace(bstack1l1_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ග"), bstack1llllll1_opy_.framework)
    file_name = bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩඝ")
    file_path = os.path.abspath(file_name)
    bstack1llll1l11_opy_ = open(file_path, bstack1l1_opy_ (u"ࠧࡸࠩඞ"))
    bstack1llll1l11_opy_.write(bstack11l1l1_opy_)
    bstack1llll1l11_opy_.close()
    logger.info(bstack1l111l11_opy_)
  except Exception as e:
    logger.error(bstack11l1ll11_opy_.format(str(e)))
def bstack11111l_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  bstack111lll1l_opy_()
  logger.debug(bstack1l11l11_opy_.format(str(CONFIG)))
  bstack11l11l_opy_()
  atexit.register(bstack1llll1ll_opy_)
  signal.signal(signal.SIGINT, bstack11ll1l1_opy_)
  signal.signal(signal.SIGTERM, bstack11ll1l1_opy_)
def bstack1lll1l11l_opy_(bstack1l1ll111_opy_, size):
  bstack111ll1l_opy_ = []
  while len(bstack1l1ll111_opy_) > size:
    bstack1ll1l111_opy_ = bstack1l1ll111_opy_[:size]
    bstack111ll1l_opy_.append(bstack1ll1l111_opy_)
    bstack1l1ll111_opy_   = bstack1l1ll111_opy_[size:]
  bstack111ll1l_opy_.append(bstack1l1ll111_opy_)
  return bstack111ll1l_opy_
def run_on_browserstack():
  if len(sys.argv) <= 1:
    logger.critical(bstack1111l111_opy_)
    return
  if sys.argv[1] == bstack1l1_opy_ (u"ࠨ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫඟ")  or sys.argv[1] == bstack1l1_opy_ (u"ࠩ࠰ࡺࠬච"):
    logger.info(bstack1l1_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡓࡽࡹ࡮࡯࡯ࠢࡖࡈࡐࠦࡶࡼࡿࠪඡ").format(__version__))
    return
  if sys.argv[1] == bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪජ"):
    bstack11lll1_opy_()
    return
  args = sys.argv
  bstack11111l_opy_()
  global CONFIG
  global bstack1ll111l_opy_
  global bstack11lllll_opy_
  global bstack1lll1ll11_opy_
  global bstack1ll1llll_opy_
  bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠬ࠭ඣ")
  if args[1] == bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඤ") or args[1] == bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨඥ"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨඦ")
    args = args[2:]
  elif args[1] == bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨට"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩඨ")
    args = args[2:]
  elif args[1] == bstack1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪඩ"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫඪ")
    args = args[2:]
  elif args[1] == bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧණ"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨඬ")
    args = args[2:]
  elif args[1] == bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨත"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩථ")
    args = args[2:]
  elif args[1] == bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪද"):
    bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫධ")
    args = args[2:]
  else:
    if not bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨන") in CONFIG or str(CONFIG[bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ඲")]).lower() in [bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧඳ"), bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩප")]:
      bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩඵ")
      args = args[1:]
    elif str(CONFIG[bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭බ")]).lower() == bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪභ"):
      bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫම")
      args = args[1:]
    elif str(CONFIG[bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩඹ")]).lower() == bstack1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ය"):
      bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧර")
      args = args[1:]
    elif str(CONFIG[bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ඼")]).lower() == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪල"):
      bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ඾")
      args = args[1:]
    elif str(CONFIG[bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ඿")]).lower() == bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ව"):
      bstack1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧශ")
      args = args[1:]
    else:
      bstack1lll1111_opy_(bstack1llll1l1_opy_)
  global bstack11llll1l_opy_
  global bstack111l1l1_opy_
  global bstack1ll1l1_opy_
  global bstack111l1l11_opy_
  global bstack11llll11_opy_
  global bstack11l1l111_opy_
  global bstack111l1lll_opy_
  global bstack1l11l11l_opy_
  global bstack11l1l11l_opy_
  global bstack1lll1l1ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
  except Exception as e:
    bstack1ll1111_opy_(e, bstack1111111l_opy_)
  bstack11llll1l_opy_ = webdriver.Remote.__init__
  bstack1l11l11l_opy_ = WebDriver.close
  if (bstack1ll1ll1_opy_ in [bstack1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧෂ"), bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨස"), bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫහ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
      from pabot.pabot import QueueItem
      from pabot import pabot
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1l1ll1l1_opy_)
    bstack111l1l1_opy_ = Output.end_test
    bstack1ll1l1_opy_ = TestStatus.__init__
    bstack111l1l11_opy_ = WebDriverCreator._get_ff_profile
    bstack11llll11_opy_ = pabot._run
    bstack11l1l111_opy_ = QueueItem.__init__
    bstack111l1lll_opy_ = pabot._create_command_for_execution
  if bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫළ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1ll1ll1l_opy_)
    bstack11l1l11l_opy_ = Runner.run_hook
    bstack1lll1l1ll_opy_ = Step.run
  if bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬෆ"):
    bstack1llll11ll_opy_()
    bstack1llll1lll_opy_()
    if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෇") in CONFIG:
      bstack11lllll_opy_ = True
      bstack1l1l11ll_opy_ = []
      for index, platform in enumerate(CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ෈")]):
        bstack1l1l11ll_opy_.append(threading.Thread(name=str(index),
                                      target=bstack1lll1l1l1_opy_, args=(args[0], index)))
      for t in bstack1l1l11ll_opy_:
        t.start()
      for t in bstack1l1l11ll_opy_:
        t.join()
    else:
      bstack1lllll11_opy_(bstack1lll1_opy_)
      exec(open(args[0]).read())
  elif bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ෉") or bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ්"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1l1ll1l1_opy_)
    bstack1llll11ll_opy_()
    bstack1lllll11_opy_(bstack111l_opy_)
    if bstack1l1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ෋") in args:
      i = args.index(bstack1l1_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ෌"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1ll111l_opy_))
    args.insert(0, str(bstack1l1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ෍")))
    pabot.main(args)
  elif bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ෎"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1l1ll1l1_opy_)
    for a in args:
      if bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ා") in a:
        bstack1lll1ll11_opy_ = int(a.split(bstack1l1_opy_ (u"ࠨ࠼ࠪැ"))[1])
      if bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ෑ") in a:
        bstack1ll1llll_opy_ = str(a.split(bstack1l1_opy_ (u"ࠪ࠾ࠬි"))[1])
    bstack1lllll11_opy_(bstack111l_opy_)
    run_cli(args)
  elif bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫී"):
    try:
      from _pytest.config import _prepareconfig
      import importlib
      bstack111ll1ll_opy_ = importlib.find_loader(bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧු"))
      if bstack111ll1ll_opy_ is None:
        bstack1ll1111_opy_(e, bstack1lll11l1_opy_)
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1lll11l1_opy_)
    bstack1llll11ll_opy_()
    try:
      if bstack1l1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨ෕") in args:
        i = args.index(bstack1l1_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩූ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ෗") in args:
        i = args.index(bstack1l1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪෘ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1_opy_ (u"ࠪ࠱ࡳ࠭ෙ") in args:
        i = args.index(bstack1l1_opy_ (u"ࠫ࠲ࡴࠧේ"))
        args.pop(i+1)
        args.pop(i)
    except Exception as exc:
      logger.error(str(exc))
    config = _prepareconfig(args)
    bstack11lll11_opy_ = config.args
    bstack11ll1lll_opy_ = config.invocation_params.args
    bstack11ll1lll_opy_ = list(bstack11ll1lll_opy_)
    bstack1l1l1ll1_opy_ = []
    for arg in bstack11ll1lll_opy_:
      if arg not in bstack11lll11_opy_:
        bstack1l1l1ll1_opy_.append(arg)
    bstack1l1l1ll1_opy_.append(bstack1l1_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧෛ"))
    bstack1l1l1ll1_opy_.append(bstack1l1_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬො"))
    bstack11llll1_opy_ = []
    for spec in bstack11lll11_opy_:
      bstack11ll11_opy_ = []
      bstack11ll11_opy_.append(spec)
      bstack11ll11_opy_ += bstack1l1l1ll1_opy_
      bstack11llll1_opy_.append(bstack11ll11_opy_)
    bstack11lllll_opy_ = True
    bstack1lll111_opy_ = 1
    if bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧෝ") in CONFIG:
      bstack1lll111_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨෞ")]
    bstack1111111_opy_ = int(bstack1lll111_opy_)*int(len(CONFIG[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬෟ")]))
    execution_items = []
    for index, _ in enumerate(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭෠")]):
      for bstack11ll11_opy_ in bstack11llll1_opy_:
        item = {}
        item[bstack1l1_opy_ (u"ࠫࡦࡸࡧࠨ෡")] = bstack11ll11_opy_
        item[bstack1l1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ෢")] = index
        execution_items.append(item)
    bstack1l1l1l_opy_ = bstack1lll1l11l_opy_(execution_items, bstack1111111_opy_)
    for execution_item in bstack1l1l1l_opy_:
      bstack1l1l11ll_opy_ = []
      for item in execution_item:
        bstack1l1l11ll_opy_.append(threading.Thread(name=str(item[bstack1l1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ෣")]),
                                            target=bstack11111l11_opy_,
                                            args=(item[bstack1l1_opy_ (u"ࠧࡢࡴࡪࠫ෤")],)))
      for t in bstack1l1l11ll_opy_:
        t.start()
      for t in bstack1l1l11ll_opy_:
        t.join()
  elif bstack1ll1ll1_opy_ == bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ෥"):
    try:
      from behave.__main__ import main as bstack111l1ll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll1111_opy_(e, bstack1ll1ll1l_opy_)
    bstack1llll11ll_opy_()
    bstack11lllll_opy_ = True
    bstack1lll111_opy_ = 1
    if bstack1l1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ෦") in CONFIG:
      bstack1lll111_opy_ = CONFIG[bstack1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ෧")]
    bstack1111111_opy_ = int(bstack1lll111_opy_)*int(len(CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ෨")]))
    config = Configuration(args)
    bstack11lll11_opy_ = config.paths
    bstack111llll1_opy_ = []
    for arg in args:
      if arg not in bstack11lll11_opy_:
        bstack111llll1_opy_.append(arg)
    bstack11llll1_opy_ = []
    for spec in bstack11lll11_opy_:
      bstack11ll11_opy_ = []
      bstack11ll11_opy_ += bstack111llll1_opy_
      bstack11ll11_opy_.append(spec)
      bstack11llll1_opy_.append(bstack11ll11_opy_)
    execution_items = []
    for index, _ in enumerate(CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෩")]):
      for bstack11ll11_opy_ in bstack11llll1_opy_:
        item = {}
        item[bstack1l1_opy_ (u"࠭ࡡࡳࡩࠪ෪")] = bstack1l1_opy_ (u"ࠧࠡࠩ෫").join(bstack11ll11_opy_)
        item[bstack1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ෬")] = index
        execution_items.append(item)
    bstack1l1l1l_opy_ = bstack1lll1l11l_opy_(execution_items, bstack1111111_opy_)
    for execution_item in bstack1l1l1l_opy_:
      bstack1l1l11ll_opy_ = []
      for item in execution_item:
        bstack1l1l11ll_opy_.append(threading.Thread(name=str(item[bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ෭")]),
                                            target=bstack111111ll_opy_,
                                            args=(item[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࠧ෮")],)))
      for t in bstack1l1l11ll_opy_:
        t.start()
      for t in bstack1l1l11ll_opy_:
        t.join()
  else:
    bstack1lll1111_opy_(bstack1llll1l1_opy_)