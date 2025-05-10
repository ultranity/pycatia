from pycatia.analysis_interfaces.analysis_document import AnalysisDocument
from pycatia.cat_mat_interfaces.material_document import MaterialDocument
from pycatia.components_catalogs_interfaces.catalog_document import CatalogDocument
from pycatia.dmaps_interfaces.process_document import ProcessDocument
from pycatia.drafting_interfaces.drawing_document import DrawingDocument
from pycatia.funct_system_interfaces.functional_document import FunctionalDocument
from pycatia.in_interfaces.document import Document
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.product_structure_interfaces.product_document import ProductDocument

document_types = {
    "Analysis": {
        "extension": "CATAnalysis",
        "type": AnalysisDocument,
    },
    "CatalogDocument": {
        "extension": "catalog",
        "type": CatalogDocument,
    },
    "CATMaterial": {
        "extension": "CATMaterial",
        "type": MaterialDocument,
    },
    "CATProcess": {
        "extension": "CATProcess",
        "type": ProcessDocument,
    },
    "cgm": {
        "extension": "cgm",
        "type": Document,
    },
    "Drawing": {
        "extension": "CATDrawing",
        "type": DrawingDocument,
    },
    "FeatureDictionary": {"extension": "CATfct", "type": Document},
    "gl": {
        "extension": "gl",
        "type": Document,
    },
    "gl2": {
        "extension": "gl2",
        "type": Document,
    },
    "hpgl": {"extension": "hpgl", "type": Document},
    "FunctionalSystem": {
        "extension": "CATSystem",
        "type": FunctionalDocument,
    },
    "Part": {
        "extension": "CATPart",
        "type": PartDocument,
    },
    "Product": {"extension": "CATProduct", "type": ProductDocument},
    "ProcessLibrary": {
        "extension": "act",
        "type": ProcessDocument,
    },
    "Default": {"extension": None, "type": Document},
}
