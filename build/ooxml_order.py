# -*- coding: utf-8 -*-
"""Insertion d'éléments OOXML dans l'ordre imposé par le schéma.

Word tolère mal les enfants désordonnés dans les propriétés (tblPr, pPr,
sectPr, tcPr, trPr) : il peut signaler un contenu illisible. Ce module
garantit l'ordre canonique quel que soit l'ordre des appels.
"""
from docx.oxml.ns import qn

ORDERS = {
    "w:tblPr": ["w:tblStyle", "w:tblpPr", "w:tblOverlap", "w:bidiVisual",
                "w:tblStyleRowBandSize", "w:tblStyleColBandSize", "w:tblW", "w:jc",
                "w:tblCellSpacing", "w:tblInd", "w:tblBorders", "w:shd", "w:tblLayout",
                "w:tblCellMar", "w:tblLook", "w:tblCaption", "w:tblDescription"],
    "w:pPr": ["w:pStyle", "w:keepNext", "w:keepLines", "w:pageBreakBefore", "w:framePr",
              "w:widowControl", "w:numPr", "w:suppressLineNumbers", "w:pBdr", "w:shd",
              "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
              "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
              "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
              "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
              "w:textDirection", "w:textAlignment", "w:textboxTightWrap",
              "w:outlineLvl", "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr",
              "w:pPrChange"],
    "w:sectPr": ["w:footnotePr", "w:endnotePr", "w:type", "w:pgSz", "w:pgMar",
                 "w:paperSrc", "w:pgBorders", "w:lnNumType", "w:pgNumType", "w:cols",
                 "w:formProt", "w:vAlign", "w:noEndnote", "w:titlePg",
                 "w:textDirection", "w:bidi", "w:rtlGutter", "w:docGrid",
                 "w:printerSettings", "w:sectPrChange"],
    "w:tcPr": ["w:cnfStyle", "w:tcW", "w:gridSpan", "w:hMerge", "w:vMerge",
               "w:tcBorders", "w:shd", "w:noWrap", "w:tcMar", "w:textDirection",
               "w:tcFitText", "w:vAlign", "w:hideMark", "w:headers", "w:cellIns",
               "w:cellDel", "w:cellMerge", "w:tcPrChange"],
    "w:trPr": ["w:cnfStyle", "w:divId", "w:gridBefore", "w:gridAfter", "w:wBefore",
               "w:wAfter", "w:cantSplit", "w:trHeight", "w:tblHeader",
               "w:tblCellSpacing", "w:jc", "w:hidden", "w:ins", "w:del",
               "w:trPrChange"],
    "w:rPr": ["w:rStyle", "w:rFonts", "w:b", "w:bCs", "w:i", "w:iCs", "w:caps",
              "w:smallCaps", "w:strike", "w:dstrike", "w:outline", "w:shadow",
              "w:emboss", "w:imprint", "w:noProof", "w:snapToGrid", "w:vanish",
              "w:webHidden", "w:color", "w:spacing", "w:w", "w:kern", "w:position",
              "w:sz", "w:szCs", "w:highlight", "w:u", "w:effect", "w:bdr", "w:shd",
              "w:fitText", "w:vertAlign", "w:rtl", "w:cs", "w:em", "w:lang",
              "w:eastAsianLayout", "w:specVanish", "w:oMath"],
}


def _tag(el):
    t = el.tag
    if "}" in t:
        ns, local = t.split("}", 1)
        return "w:" + local
    return t


def insert_ordered(parent, element):
    """Insère `element` dans `parent` en respectant l'ordre du schéma."""
    order = ORDERS.get(_tag(parent))
    if order is None:
        parent.append(element)
        return element
    name = _tag(element)
    try:
        idx = order.index(name)
    except ValueError:
        parent.append(element)
        return element
    # premier frère dont l'ordre est strictement supérieur
    for i, child in enumerate(list(parent)):
        cn = _tag(child)
        pos = order.index(cn) if cn in order else len(order)
        if pos > idx:
            parent.insert(i, element)
            return element
    parent.append(element)
    return element


def set_child(parent, element):
    """Remplace (ou insère) l'élément du même nom."""
    for old in parent.findall(qn(_tag(element))):
        parent.remove(old)
    return insert_ordered(parent, element)
