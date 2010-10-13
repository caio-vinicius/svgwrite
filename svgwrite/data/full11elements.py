#coding:utf-8

from types import SVGElement

presentation_attributes = frozenset([ "alignment-baseline", "baseline-shift",
    "clip", "clip-path", "clip-rule", "color", "color-interpolation",
    "color-interpolation-filters", "color-profile", "color-rendering", "cursor",
    "direction", "display", "dominant-baseline", "enable-background",
    "fill", "fill-opacity", "fill-rule", "filter", "flood-color",
    "flood-opacity", "font-family", "font-size", "font-size-adjust",
    "font-stretch", "font-style", "font-variant", "font-weight",
    "glyph-orientation-horizontal", "glyph-orientation-vertical",
    "image-rendering", "kerning", "letter-spacing", "lighting-color",
    "marker-end", "marker-mid", "marker-start", "mask", "opacity",
    "overflow", "pointer-events", "shape-rendering", "stop-color",
    "stop-opacity", "stroke", "stroke-dasharray", "stroke-dashoffset",
    "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
    "stroke-opacity", "stroke-width", "text-anchor", "text-decoration",
    "text-rendering", "unicode-bidi", "visibility", "word-spacing",
    "writing-mode"])

full11_elements = {
    'a': SVGElement('a',
    attributes=frozenset(['xlink:title', 'xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'systemLanguage', 'onmouseover', 'xlink:type', 'externalResourcesRequired', 'id', 'xlink:actuate', 'onload', 'style', 'xlink:show', 'target', 'onactivate', 'nmousedown', 'transform', 'class', 'xlink:role', 'requiredFeatures', 'xml:lang', 'onmousemove', 'xmlns:xlink', 'onclick', 'xlink:arcrole', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'altGlyph': SVGElement('altGlyph',
    attributes=frozenset(['requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'id', 'onload', 'style', 'nmousedown', 'onmousemove', 'onclick', 'xlink:arcrole', 'onfocusin', 'xml:base', 'onmouseup', 'onmouseout', 'format', 'xlink:title', 'systemLanguage', 'onmouseover', 'dx', 'dy', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'xlink:show', 'onactivate', 'glyphRef', 'xlink:role', 'requiredFeatures', 'xml:lang', 'y', 'x', 'rotate']),
    properties=presentation_attributes,
    children=[]),

    'altGlyphDef': SVGElement('altGlyphDef',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'altGlyphItem': SVGElement('altGlyphItem',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'animate': SVGElement('animate',
    attributes=frozenset(['requiredExtensions', 'from', 'repeatCount', 'xml:space', 'xlink:href', 'xlink:type', 'attributeType', 'repeatDur', 'id', 'fill', 'onload', 'additive', 'calcMode', 'min', 'keySplines', 'to', 'dur', 'xlink:arcrole', 'onend', 'begin', 'xml:base', 'max', 'xlink:title', 'attributeName', 'onbegin', 'systemLanguage', 'accumulate', 'end', 'externalResourcesRequired', 'by', 'restart', 'xlink:actuate', 'xlink:show', 'xlink:role', 'requiredFeatures', 'xml:lang', 'values', 'keyTimes', 'onrepeat']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'animateColor': SVGElement('animateColor',
    attributes=frozenset(['requiredExtensions', 'from', 'repeatCount', 'xml:space', 'xlink:href', 'xlink:type', 'attributeType', 'repeatDur', 'id', 'fill', 'onload', 'additive', 'calcMode', 'min', 'keySplines', 'to', 'dur', 'xlink:arcrole', 'onend', 'begin', 'xml:base', 'max', 'xlink:title', 'attributeName', 'onbegin', 'systemLanguage', 'accumulate', 'end', 'externalResourcesRequired', 'by', 'restart', 'xlink:actuate', 'xlink:show', 'xlink:role', 'requiredFeatures', 'xml:lang', 'values', 'keyTimes', 'onrepeat']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'animateMotion': SVGElement('animateMotion',
    attributes=frozenset(['origin', 'requiredExtensions', 'from', 'repeatCount', 'xml:space', 'xlink:href', 'xlink:type', 'repeatDur', 'id', 'fill', 'onload', 'additive', 'calcMode', 'min', 'keySplines', 'to', 'dur', 'xlink:arcrole', 'onend', 'begin', 'xlink:title', 'xml:base', 'max', 'end', 'keyPoints', 'onbegin', 'systemLanguage', 'accumulate', 'path', 'externalResourcesRequired', 'by', 'restart', 'xlink:actuate', 'xlink:show', 'xlink:role', 'requiredFeatures', 'xml:lang', 'values', 'keyTimes', 'onrepeat', 'rotate']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'mpath', 'title'])),

    'animateTransform': SVGElement('animateTransform',
    attributes=frozenset(['requiredExtensions', 'from', 'repeatCount', 'xml:space', 'xlink:href', 'xlink:type', 'attributeType', 'repeatDur', 'id', 'fill', 'onload', 'additive', 'calcMode', 'min', 'keySplines', 'to', 'dur', 'xlink:arcrole', 'type', 'onend', 'begin', 'xml:base', 'max', 'xlink:title', 'attributeName', 'onbegin', 'systemLanguage', 'accumulate', 'end', 'externalResourcesRequired', 'by', 'restart', 'xlink:actuate', 'xlink:show', 'xlink:role', 'requiredFeatures', 'xml:lang', 'values', 'keyTimes', 'onrepeat']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'circle': SVGElement('circle',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'cy', 'cx', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'class', 'requiredFeatures', 'r', 'onmousemove', 'onclick', 'xml:lang', 'onfocusin', 'systemLanguage']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'metadata', 'desc'])),

    'clipPath': SVGElement('clipPath',
    attributes=frozenset(['clipPathUnits', 'style', 'xml:base', 'requiredExtensions', 'xml:space', 'transform', 'id', 'requiredFeatures', 'xml:lang', 'externalResourcesRequired', 'class', 'systemLanguage']),
    properties=presentation_attributes,
    children=frozenset(['set', 'animate', 'text', 'use', 'animateColor', 'polyline', 'path', 'line', 'ellipse', 'rect', 'desc', 'animateMotion', 'polygon', 'title', 'animateTransform', 'circle', 'metadata'])),

    'color-profile': SVGElement('color-profile',
    attributes=frozenset(['xlink:actuate', 'xlink:show', 'xml:base', 'name', 'rendering-intent', 'xml:space', 'xlink:href', 'xlink:role', 'xml:lang', 'xlink:type', 'xlink:title', 'xlink:arcrole', 'local', 'id']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'cursor': SVGElement('cursor',
    attributes=frozenset(['xlink:title', 'xml:base', 'requiredExtensions', 'xml:space', 'xlink:href', 'systemLanguage', 'xlink:type', 'externalResourcesRequired', 'id', 'xlink:actuate', 'xlink:show', 'xlink:role', 'requiredFeatures', 'xml:lang', 'y', 'x', 'xlink:arcrole']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'defs': SVGElement('defs',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'class', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'id', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'desc': SVGElement('desc',
    attributes=frozenset(['style', 'xml:lang', 'xml:base', 'xml:space', 'class', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'ellipse': SVGElement('ellipse',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'ry', 'cy', 'cx', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'onactivate', 'nmousedown', 'rx', 'transform', 'class', 'requiredFeatures', 'systemLanguage', 'onmousemove', 'onclick', 'xml:lang', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'feBlend': SVGElement('feBlend',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'in2', 'height', 'width', 'xml:lang', 'id', 'result', 'in', 'y', 'x', 'class', 'mode']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feColorMatrix': SVGElement('feColorMatrix',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'id', 'height', 'width', 'xml:lang', 'values', 'result', 'in', 'y', 'x', 'type', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feComponentTransfer': SVGElement('feComponentTransfer',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'height', 'width', 'xml:lang', 'id', 'result', 'in', 'y', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['feFuncA', 'feFuncR', 'feFuncB', 'feFuncG'])),

    'feComposite': SVGElement('feComposite',
    attributes=frozenset(['xml:base', 'xml:space', 'in2', 'height', 'result', 'in', 'operator', 'class', 'style', 'width', 'id', 'k3', 'k2', 'k1', 'xml:lang', 'k4', 'y', 'x']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feConvolveMatrix': SVGElement('feConvolveMatrix',
    attributes=frozenset(['xml:base', 'xml:space', 'kernelUnitLength', 'edgeMode', 'height', 'bias', 'result', 'in', 'preserveAlpha', 'id', 'style', 'divisor', 'kernelMatrix', 'width', 'xml:lang', 'targetX', 'targetY', 'y', 'x', 'class2', 'order']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feDiffuseLighting': SVGElement('feDiffuseLighting',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'diffuseConstant', 'height', 'kernelUnitLength', 'width', 'xml:lang', 'id', 'result', 'in', 'y', 'x', 'class', 'surfaceScale']),
    properties=presentation_attributes,
    children=frozenset(['fePointLight', 'feSpotLight', 'title', 'metadata', 'feDistantLight', 'desc'])),

    'feDisplacementMap': SVGElement('feDisplacementMap',
    attributes=frozenset(['xml:base', 'xml:space', 'yChannelSelector', 'in2', 'height', 'result', 'in', 'class', 'style', 'scale', 'id', 'width', 'xml:lang', 'xChannelSelector', 'y', 'x']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feDistantLight': SVGElement('feDistantLight',
    attributes=frozenset(['xml:lang', 'elevation', 'azimuth', 'xml:base', 'xml:space', 'id']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feFlood': SVGElement('feFlood',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'height', 'width', 'xml:lang', 'id', 'result', 'y', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set', 'animateColor'])),

    'feFuncA': SVGElement('feFuncA',
    attributes=frozenset(['slope', 'xml:base', 'tableValues', 'xml:space', 'xml:lang', 'intercept', 'amplitude', 'offset', 'type', 'id', 'exponent']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feFuncB': SVGElement('feFuncB',
    attributes=frozenset(['slope', 'xml:base', 'tableValues', 'xml:space', 'xml:lang', 'intercept', 'amplitude', 'offset', 'type', 'id', 'exponent']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feFuncG': SVGElement('feFuncG',
    attributes=frozenset(['slope', 'xml:base', 'tableValues', 'xml:space', 'xml:lang', 'intercept', 'amplitude', 'offset', 'type', 'id', 'exponent']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feFuncR': SVGElement('feFuncR',
    attributes=frozenset(['slope', 'xml:base', 'tableValues', 'xml:space', 'xml:lang', 'intercept', 'amplitude', 'offset', 'type', 'id', 'exponent']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feGaussianBlur': SVGElement('feGaussianBlur',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'height', 'width', 'xml:lang', 'id', 'result', 'in', 'y', 'x', 'stdDeviation', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feImage': SVGElement('feImage',
    attributes=frozenset(['xlink:title', 'xml:base', 'xml:space', 'xlink:href', 'height', 'result', 'xlink:type', 'externalResourcesRequired', 'preserveAsectRatio', 'class', 'xlink:actuate', 'style', 'xlink:show', 'id', 'xlink:role', 'width', 'xml:lang', 'y', 'x', 'xlink:arcrole']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set', 'animateColor'])),

    'feMerge': SVGElement('feMerge',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'height', 'width', 'xml:lang', 'id', 'result', 'y', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feMergeNode': SVGElement('feMergeNode',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id', 'in']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feMorphology': SVGElement('feMorphology',
    attributes=frozenset(['style', 'xml:base', 'y', 'xml:space', 'id', 'height', 'width', 'xml:lang', 'radius', 'result', 'in', 'operator', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feOffset': SVGElement('feOffset',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'in', 'height', 'width', 'xml:lang', 'id', 'result', 'dx', 'dy', 'y', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'fePointLight': SVGElement('fePointLight',
    attributes=frozenset(['xml:lang', 'xml:base', 'y', 'x', 'xml:space', 'z', 'id']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feSpecularLighting': SVGElement('feSpecularLighting',
    attributes=frozenset(['specularConstant', 'xml:base', 'xml:space', 'kernelUnitLength', 'height', 'result', 'in', 'class', 'style', 'id', 'width', 'xml:lang', 'specularExponent', 'y', 'x', 'surfaceScale']),
    properties=presentation_attributes,
    children=frozenset(['fePointLight', 'feSpotLight', 'title', 'metadata', 'feDistantLight', 'desc'])),

    'feSpotLight': SVGElement('feSpotLight',
    attributes=frozenset(['pointsAtX', 'xml:base', 'xml:space', 'limitingConeAngle', 'xml:lang', 'specularExponent', 'pointsAtZ', 'y', 'x', 'pointsAtY', 'z', 'id']),
    properties=[],
    children=frozenset(['animate', 'set'])),

    'feTile': SVGElement('feTile',
    attributes=frozenset(['style', 'xml:base', 'xml:space', 'height', 'width', 'xml:lang', 'id', 'result', 'in', 'y', 'x', 'class']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set'])),

    'feTurbulence': SVGElement('feTurbulence',
    attributes=frozenset(['xml:base', 'baseFrequency', 'xml:space', 'stitchTiles', 'height', 'width', 'xml:lang', 'id', 'result', 'x', 'y', 'numOctaves', 'type', 'seed']),
    properties=presentation_attributes,
    children=[]),

    'filter': SVGElement('filter',
    attributes=frozenset(['xlink:title', 'xml:base', 'xml:space', 'xlink:href', 'height', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'style', 'xlink:show', 'filterRes', 'primitiveUnits', 'id', 'xlink:role', 'width', 'xml:lang', 'y', 'x', 'xlink:arcrole', 'filterUnits']),
    properties=presentation_attributes,
    children=frozenset(['set', 'title', 'height', 'width', 'result', 'y', 'x', 'animate', 'metadata', 'desc'])),

    'font': SVGElement('font',
    attributes=frozenset(['xml:base', 'xml:space', 'R', 'id', 'a', 'c', 'e', 'd', 'g', 'i', 'h', '-', 'l', 'o', 'n', 'q', 's', 'r', 'u', 't', 'v', 'y', 'x', 'z', 'xml:lang']),
    properties=presentation_attributes,
    children=frozenset(['title', 'metadata', 'missing-glyph', 'font-face', 'vkern', 'hkern', 'glyph', 'desc'])),

    'font-face': SVGElement('font-face',
    attributes=frozenset(['mathematical', 'slope', 'font-size', 'xml:space', 'v-hanging', 'hanging', 'overline-thickness', 'ascent', 'id', 'strikethrough-position', 'underline-position', 'descent', 'cap-height', 'units-per-em', 'font-style', 'unicode-range', 'font-stretch', 'font-variant', 'x-height', 'font-weight', 'xml:base', 'panose-1', 'strikethrough-thickness', 'stemh', 'v-alphabetic', 'stemv', 'bbox', 'underline-thickness', 'font-family', 'v-mathematical', 'v-ideographic', 'ideographic', 'overline-position', 'widths', 'xml:lang', 'accent-height', 'alphabetic']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'font-face-src', 'title'])),

    'font-face-format': SVGElement('font-face-format',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id']),
    properties=[],
    children=[]),

    'font-face-name': SVGElement('font-face-name',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id', 'name']),
    properties=[],
    children=[]),

    'font-face-uri': SVGElement('font-face-uri',
    attributes=frozenset(['xlink:actuate', 'xlink:show', 'xml:base', 'xml:space', 'xlink:href', 'xlink:role', 'xml:lang', 'xlink:type', 'xlink:title', 'xlink:arcrole', 'id']),
    properties=[],
    children=frozenset(['font-face-format'])),

    'foreignObject': SVGElement('foreignObject',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'height', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'class', 'width', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'y', 'x', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['*'])),

    'g': SVGElement('g',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'class', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'id', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'glyph': SVGElement('glyph',
    attributes=frozenset(['xml:base', 'm', 'xml:space', 'id', 'a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', '-', 'l', 'o', 'n', 'p', 's', 'r', 'u', 't', 'v', 'y', 'x', 'z', 'xml:lang']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'glyphRef': SVGElement('glyphRef',
    attributes=frozenset(['xlink:title', 'xml:base', 'format', 'xml:space', 'xlink:href', 'dx', 'dy', 'xlink:type', 'class', 'xlink:actuate', 'style', 'xlink:show', 'id', 'xlink:role', 'xml:lang', 'y', 'x', 'xlink:arcrole', 'glyphRef']),
    properties=presentation_attributes,
    children=[]),

    'hkern': SVGElement('hkern',
    attributes=frozenset(['xml:base', 'g2', 'g1', 'xml:space', 'u1', 'u2', 'xml:lang', 'id', 'k']),
    properties=[],
    children=[]),

    'image': SVGElement('image',
    attributes=frozenset(['requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'height', 'id', 'onload', 'style', 'nmousedown', 'transform', 'width', 'onmousemove', 'onclick', 'xlink:arcrole', 'onfocusin', 'xml:base', 'onmouseup', 'onmouseout', 'xlink:title', 'systemLanguage', 'onmouseover', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'xlink:show', 'onactivate', 'xlink:role', 'requiredFeatures', 'xml:lang', 'y', 'x', 'preserveAspectRatio']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'line': SVGElement('line',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'x2', 'systemLanguage', 'onmouseover', 'y1', 'externalResourcesRequired', 'y2', 'id', 'onload', 'style', 'x1', 'onactivate', 'nmousedown', 'transform', 'class', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'linearGradient': SVGElement('linearGradient',
    attributes=frozenset(['xlink:title', 'xml:base', 'xml:space', 'xlink:href', 'x2', 'y1', 'externalResourcesRequired', 'y2', 'class', 'xlink:actuate', 'xlink:role', 'style', 'xlink:show', 'spreadMethod', 'id', 'gradientUnits', 'xml:lang', 'gradientTransform', 'xlink:type', 'xlink:arcrole', 'x1']),
    properties=presentation_attributes,
    children=frozenset(['set', 'title', 'animate', 'animateTransform', 'stop', 'metadata', 'desc'])),

    'marker': SVGElement('marker',
    attributes=frozenset(['xml:space', 'id', 'xml:lang', 'A', 'B', 'xml:base', 'H', 'R', 'U', 'W', 'Y', 'X', 'a', 'c', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'm', 'l', 'o', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'mask': SVGElement('mask',
    attributes=frozenset(['xml:base', 'requiredExtensions', 'xml:space', 'height', 'systemLanguage', 'externalResourcesRequired', 'maskContentUnits', 'class', 'style', 'id', 'width', 'requiredFeatures', 'xml:lang', 'y', 'x', 'maskUnits']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'metadata': SVGElement('metadata',
    attributes=frozenset(['xml:space', 'xml:lang', 'xml:base', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'missing-glyph': SVGElement('missing-glyph',
    attributes=frozenset(['xml:base', 'xml:space', 'id', 'a', 'c', 'e', 'd', 'g', 'i', 'h', '-', 'l', 'o', 'n', 's', 'r', 't', 'v', 'y', 'x', 'z', 'xml:lang']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'mpath': SVGElement('mpath',
    attributes=frozenset(['xlink:actuate', 'xlink:show', 'xml:base', 'xml:space', 'xlink:href', 'id', 'xlink:role', 'xml:lang', 'xlink:type', 'xlink:title', 'xlink:arcrole', 'externalResourcesRequired']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'path': SVGElement('path',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'pathLength', 'externalResourcesRequired', 'id', 'onload', 'style', 'd', 'onactivate', 'nmousedown', 'transform', 'class', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'pattern': SVGElement('pattern',
    attributes=frozenset(['xlink:title', 'xml:base', 'requiredExtensions', 'xml:space', 'xlink:href', 'height', 'class', 'systemLanguage', 'patternContentUnits', 'xlink:type', 'externalResourcesRequired', 'id', 'xlink:actuate', 'style', 'xlink:show', 'viewBox', 'xlink:role', 'width', 'requiredFeatures', 'patternUnits', 'patternTransform', 'y', 'x', 'preserveAspectRatio', 'xlink:arcrole', 'xml:lang']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'polygon': SVGElement('polygon',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'class', 'requiredFeatures', 'points', 'onmousemove', 'onclick', 'xml:lang', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'polyline': SVGElement('polyline',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'class', 'requiredFeatures', 'points', 'onmousemove', 'onclick', 'xml:lang', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'radialGradient': SVGElement('radialGradient',
    attributes=frozenset(['xlink:title', 'xml:base', 'fx', 'fy', 'xml:space', 'xlink:href', 'cy', 'cx', 'xlink:type', 'externalResourcesRequired', 'r', 'id', 'xlink:actuate', 'gradientUnits', 'style', 'xlink:show', 'spreadMethod', 'class', 'xlink:role', 'xml:lang', 'gradientTransform', 'xlink:arcrole']),
    properties=presentation_attributes,
    children=frozenset(['set', 'title', 'animate', 'animateTransform', 'stop', 'metadata', 'desc'])),

    'rect': SVGElement('rect',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'height', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'id', 'onload', 'style', 'ry', 'onactivate', 'nmousedown', 'rx', 'transform', 'class', 'width', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'y', 'x', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'metadata', 'desc'])),

    'script': SVGElement('script',
    attributes=frozenset(['xlink:actuate', 'xlink:show', 'xml:base', 'xml:space', 'xlink:href', 'id', 'xlink:role', 'xml:lang', 'xlink:type', 'xlink:title', 'xlink:arcrole', 'type', 'externalResourcesRequired']),
    properties=[],
    children=[]),

    'set': SVGElement('set',
    attributes=frozenset(['begin', 'xlink:title', 'xml:base', 'requiredExtensions', 'repeatCount', 'xml:space', 'xlink:href', 'attributeName', 'onbegin', 'systemLanguage', 'attributeType', 'xlink:type', 'externalResourcesRequired', 'id', 'restart', 'fill', 'xlink:actuate', 'onload', 'xlink:show', 'end', 'min', 'repeatDur', 'xlink:role', 'to', 'requiredFeatures', 'xml:lang', 'max', 'dur', 'xlink:arcrole', 'onrepeat', 'onend']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'stop': SVGElement('stop',
    attributes=frozenset(['a', 'c', 'xml:base', 'f', 'xml:space', 'l', 'o', 's', 'xml:lang', 't', 'y', 'e', 'id']),
    properties=presentation_attributes,
    children=frozenset(['animate', 'set', 'animateColor'])),

    'style': SVGElement('style',
    attributes=frozenset(['xml:lang', 'xml:base', 'title', 'media', 'xml:space', 'type', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'svg': SVGElement('svg',
    attributes=frozenset(['requiredExtensions', 'onerror', 'onfocusout', 'xml:space', 'height', 'onscroll', 'baseProfile', 'contentStyleType', 'id', 'onabort', 'onload', 'style', 'nmousedown', 'onzoom', 'onresize', 'width', 'version', 'onmousemove', 'onmouseup', 'xmlns:xlink', 'xmlns:ev', 'onfocusin', 'xml:base', 'onclick', 'onmouseout', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'zoomAndPan', 'class', 'onunload', 'xmlns', 'onactivate', 'viewBox', 'requiredFeatures', 'xml:lang', 'y', 'x', 'preserveAspectRatio', 'contentScriptType']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'switch': SVGElement('switch',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'systemLanguage', 'onmouseover', 'externalResourcesRequired', 'class', 'onload', 'style', 'onactivate', 'nmousedown', 'transform', 'id', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'line', 'use', 'animateColor', 'polyline', 'path', 'animate', 'ellipse', 'rect', 'desc', 'a', 'animateMotion', 'polygon', 'g', 'title', 'svg', 'switch', 'animateTransform', 'foreignObject', 'circle', 'metadata'])),

    'symbol': SVGElement('symbol',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'onfocusout', 'xml:space', 'onmouseover', 'id', 'externalResourcesRequired', 'viewBox', 'onload', 'style', 'onactivate', 'nmousedown', 'class', 'xml:lang', 'onmousemove', 'onclick', 'preserveAspectRatio', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['set', 'text', 'image', 'font-face', 'polyline', 'marker', 'animate', 'font', 'color-profile', 'ellipse', 'cursor', 'style', 'polygon', 'title', 'pattern', 'circle', 'radialGradient', 'metadata', 'defs', 'symbol', 'use', 'animateMotion', 'animateColor', 'path', 'line', 'rect', 'desc', 'a', 'g', 'svg', 'script', 'mask', 'altGlyphDef', 'filter', 'switch', 'animateTransform', 'linearGradient', 'clipPath', 'foreignObject', 'view'])),

    'text': SVGElement('text',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'class', 'systemLanguage', 'onmouseover', 'dx', 'dy', 'externalResourcesRequired', 'lengthAdjust', 'onload', 'style', 'rotate', 'onactivate', 'nmousedown', 'textLength', 'transform', 'id', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'y', 'x', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['a', 'animateMotion', 'set', 'title', 'textPath', 'tspan', 'animateColor', 'tref', 'animateTransform', 'altGlyph', 'animate', 'desc', 'metadata'])),

    'textPath': SVGElement('textPath',
    attributes=frozenset(['requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'startOffset', 'id', 'onload', 'style', 'nmousedown', 'lengthAdjust', 'onmousemove', 'onclick', 'xlink:arcrole', 'onfocusin', 'xml:base', 'onmouseup', 'onmouseout', 'xlink:title', 'spacing', 'systemLanguage', 'onmouseover', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'xlink:show', 'onactivate', 'textLength', 'method', 'xlink:role', 'requiredFeatures', 'xml:lang']),
    properties=presentation_attributes,
    children=frozenset(['a', 'set', 'title', 'tspan', 'animateColor', 'tref', 'altGlyph', 'animate', 'metadata', 'desc'])),

    'title': SVGElement('title',
    attributes=frozenset(['style', 'xml:lang', 'xml:base', 'xml:space', 'class', 'id']),
    properties=[],
    children=frozenset(['*'])),

    'tref': SVGElement('tref',
    attributes=frozenset(['requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'id', 'onload', 'style', 'nmousedown', 'lengthAdjust', 'onmousemove', 'onclick', 'xlink:arcrole', 'onfocusin', 'xml:base', 'onmouseup', 'onmouseout', 'xlink:title', 'systemLanguage', 'onmouseover', 'dx', 'dy', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'xlink:show', 'onactivate', 'textLength', 'xlink:role', 'requiredFeatures', 'xml:lang', 'y', 'x', 'rotate']),
    properties=presentation_attributes,
    children=frozenset(['set', 'title', 'animate', 'metadata', 'animateColor', 'desc'])),

    'tspan': SVGElement('tspan',
    attributes=frozenset(['xml:base', 'onmouseup', 'onmouseout', 'requiredExtensions', 'onfocusout', 'xml:space', 'class', 'systemLanguage', 'onmouseover', 'dx', 'dy', 'externalResourcesRequired', 'lengthAdjust', 'onload', 'style', 'rotate', 'onactivate', 'nmousedown', 'textLength', 'id', 'requiredFeatures', 'xml:lang', 'onmousemove', 'onclick', 'y', 'x', 'onfocusin']),
    properties=presentation_attributes,
    children=frozenset(['a', 'set', 'title', 'tspan', 'animateColor', 'tref', 'altGlyph', 'animate', 'metadata', 'desc'])),

    'use': SVGElement('use',
    attributes=frozenset(['requiredExtensions', 'onfocusout', 'xml:space', 'xlink:href', 'height', 'id', 'onload', 'style', 'nmousedown', 'transform', 'width', 'onmousemove', 'onclick', 'xlink:arcrole', 'onfocusin', 'xml:base', 'onmouseup', 'onmouseout', 'xlink:title', 'systemLanguage', 'onmouseover', 'xlink:type', 'externalResourcesRequired', 'class', 'xlink:actuate', 'xlink:show', 'onactivate', 'xlink:role', 'requiredFeatures', 'xml:lang', 'y', 'x']),
    properties=presentation_attributes,
    children=frozenset(['animateMotion', 'set', 'title', 'animateColor', 'animateTransform', 'animate', 'desc', 'metadata'])),

    'view': SVGElement('view',
    attributes=frozenset(['xml:base', 'viewTarget', 'xml:space', 'viewBox', 'xml:lang', 'preserveAspectRatio', 'externalResourcesRequired', 'zoomAndPan', 'id']),
    properties=[],
    children=frozenset(['desc', 'metadata', 'title'])),

    'vkern': SVGElement('vkern',
    attributes=frozenset(['xml:base', 'g2', 'g1', 'xml:space', 'u1', 'u2', 'xml:lang', 'id', 'k']),
    properties=[],
    children=[]),

}
