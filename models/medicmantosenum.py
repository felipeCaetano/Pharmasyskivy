from enum import Enum


class Tarja(Enum):
    tipo = 'Tarja:'
    sem_tarja = 'Sem Tarja'
    vermelha = 'Vermelha'
    vermelharest = 'Vermelha restr.'
    preta = 'Preta'

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class FormaFarmaceutica(Enum):
    choice = ('Forma Farmaceutica:', "")
    adesivo = ("ADESIVO", "ADES")
    anel = ("ANEL", "ANEL")
    barra = ('BARRA', "BAR")
    bastao = ("BASTÃO", "BAST")
    capsula = ('CÁPSULA', "CAP")
    comprimido = ('COMPRIMIDO', "COM")
    diu = ('DIU', "DIU")
    filme = ('FILME', "FIL")
    globulo = ('GLÓBULO', "GLOB")
    goma = ('GOMA DE MASCAR', "GOMA")
    granulado = ('GRANULADO', "GRAN")
    implante = ('IMPLANTE', "IMPL")
    pastilha = ('PASTILHA', "PAS")
    po = ('PÓ', "PO")
    rasura = ('RASURA', "RAS")
    sabonete = ('SABONETE', "SAB")
    supositorio = ('SUPOSITÓRIO', "SUP")
    tablete = ('TABLETE', "TABLE")
    emulsao = ('EMULSÃO', "EMU")
    esmalte = ('ESMALTE', "ESM")
    espuma = ('ESPUMA', "ESP")
    liquido = ('LÍQUIDO', "LIQ")
    oleo = ("ÓLEO", "OLE")
    saboneteliqd = ('SABONETE LIQUIDO', "SAB LIQ")
    solucao = ('SOLUÇÃO', "SOL")
    colutorio = ('COLUTÓRIO', "COL")
    elixir = ('ELIXIR', "ELX")
    suspencao = ('SUSPENÇÃO', "SUS")
    xampu = ('XAMPU', "XAMP")
    xarope = ('XAROPE', "XPE")
    creme = ('CREME', "CREM")
    emplasto = ('EMPLASTO', "EMPL")
    gel = ('GEL', "GEL")
    pomada = ('POMADA', "POM")
    gas = ('GÁS', "GAS")

    @classmethod
    def list_names(cls):
        lista = [member.value[0] for member in cls]
        return lista

    @classmethod
    def list_abreviacao(cls):
        lista = [member.value[1] for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value[0]} for member in cls]
        return lista


class ClasseTerapeutica(Enum):
    nenhum = "Classe Terapeutica:"
    A02A = 'Antiácidos'
    A02D = 'Antiflatulentes'
    A02X = "Outros antiacidos event medicamentos para ulcera event da  " \
           "flatulencia"
    Analgesico = 'Analgésicos'
    Anestesico = 'Anestésicos'
    Anorexigeno = 'Anorexigenos'
    Ansiolitico = 'Ansiolíticos'
    a_hemor = 'Anti-hemorrágicos'
    a_hiperten = 'Anti-hipertensivos'
    a_histam = 'Anti-histamínicos'
    a_infne = 'Anti-inflamatórios não esteróides'
    a_agreg = 'Antiagregantes'
    a_anemic = 'Antianemicos'
    a_arritm = 'Antiarritmicos'
    a_asmat = 'Antiasmáticos'
    a_biotic = 'Antibióticos'
    a_coagul = 'Anticoagulantes'
    a_colica = 'Anticólica'
    a_concep = 'Anticoncepcionais'
    a_convul = 'Anticonvulsivantes'
    a_depres = 'Antidepressivos'
    a_diabet = 'Antidiabéticos'
    A03A = "Antiespasmodicos event anticolinérgicos sintéticos"
    A03C = "Antiespasmodicos em associação com psicolépticos"
    A03D = "Antiespasmodicos em associação com analgésicos"
    A03B = "Beladona event derivados simples"
    A03F = "Propulsivos"
    A07 = 'Antidiarreicos'
    A07A = 'Antiinfeciosos intestinais'
    A07C = 'Elactrólitos com hidratos de carbono'
    A07D = 'Antiprupulsivos'
    A07E = 'Antiinflamatórios instestinais'
    A07F = 'Microorganismos antidiarréicos'
    A08 = 'Preparados antiobesidade, excluindo dietéticos'
    A04 = 'Antieméticos event Antinauseantes'
    A05A = 'Terapêutica Biliar'
    A05B = 'Terapêutica hepática lipotrópicos'
    A05C = 'Medicamentos para Terapêutica biliar event hepática  ' \
           'associados'
    A10A = "Insulinas"
    a_fungic = 'Antifúngicos'
    a_grips = 'Antigripais'
    a_inftop = 'Anti-inflamatorio Topico'
    a_lipem = 'Antilipemicos'
    a_lipemrc = 'Antilipemicos - Redutores do colesterol'
    a_mico = 'Antimicoticos'
    a_micos = 'Antimicoticos Sistemicos'
    a_micot = 'Antimicoticos Topicos'
    a_paras = 'Antiparasitários'
    a_park = 'Antiparkinsonianos'
    a_piret = 'Antipiréticos'
    a_psic = 'Antipsicóticos'
    a_sept_or = 'Antissepticos Orais'
    a_termic = 'Antitérmicos'
    a_tuss = 'Antitussígenos'
    a_ulcer = 'Antiulcerosos'
    a_varic = 'Antivaricosos'
    a_vertig = 'Antivertiginosos'
    A11B = "Multivitaminas, associação"
    A11C = "Multivitaminas, simples"
    A13 = "Tonicos"
    a_virais = 'Antivirais'
    ativador = 'Ativadores do Metabolismo Cerebral'
    benzod = 'Benzodiazepinas'
    betab = 'Betabloqueadores'
    bifosf = 'Bifosfonatos'
    broncod = 'Broncodilatadores'
    cardiot = 'Cardiotônicos'
    cicatriz = 'Cicatrizantes'
    coenzim = 'Coenzimas'
    cortic = 'Corticóides'
    cortic_s = 'Corticosteroides Sistemicos'
    cortic_t = 'Corticosteroides Topicos'
    Defatig = 'Defatigantes'
    descong = 'Descongestionantes nasais'
    diuret = 'Diuréticos'
    eletrol = 'Eletrolitos'
    A09 = 'Digestivos, incluindo Enzimas'
    pancreas = 'Pancreáticas'
    A15 = 'Estimulantes do Apetite'
    A16 = 'outros produtos para as vias digestivas event metabolismo'
    estimul_r = 'Estimulantes respiratórios'
    expect = 'Expectorantes'
    fitot = 'Fitoterápicos'
    sangue = 'Frações do sangue ou plasma exceto gamaglobulina'
    hepato = 'Hepatoprotetores'
    higien = 'Higiene'
    hipono = 'Hipnóticos'
    hipogli = 'Hipoglicemiantes Orais'
    homeop = 'Homeopáticos'
    hormon = 'Hormônios'
    imunomod = 'Imunomoduladores'
    imunosup = 'Imunossupressores'
    indutor = 'Indutores do Sono'
    A06 = 'Laxativos'
    manuart = 'Manutenção das articulações'
    mucol = 'Mucolíticos'
    neurole = 'Neurolepticos'
    plaquet = 'Plaquetarios'
    possos = 'Problemas ósseos'
    psico = 'Psicoanalépticos'
    relax = 'Relaxantes musculares'
    A14 = "anabolizantes"
    repel = 'Repelentes'
    sedat = 'Sedativos'
    sedat_t = 'Sedativos da Tosse'
    soliso = 'Soluções Isomóticas Salinas Simples'
    vasocon = 'Vasoconstritores'
    vasod = 'Vasodilatadores'
    A11 = 'Vitaminas'
    A12A = 'Calcio'
    A12C = 'Outros suplementos minerais'

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class UnidadeDosagem(Enum):
    unidade = 'Unidade dosagem:'
    litro = 'L'
    mililitro = 'mL'
    grama = 'g'
    miligrama = 'mg'
    kilograma = 'kg'
    micrograma = 'ug'
    gramaporlitro = 'g/L'
    miligramplitro = 'mg/L'
    gramaporml = 'g/mL'
    miligramapml = 'mg/mL'
    unidadeinter = 'UI'
    unidadeporml = 'UI/mL'
    unidadeporlitro = 'UI/L'

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class Embalagem(Enum):
    apresentacao = "Apresentação:"
    ampola = "AMPOLA"
    aplicador_preenc = "APLICADOR PREENCHIDO"
    bisnaga = "BISNAGA"
    blister = "BLÍSTER"
    bolsa = "BOLSA"
    bambona = "BAMBONA"
    carpule = "CARPULE"
    cilindro = "CILINDRO"
    envelope = "ENVELOPE"
    estojo = "ESTOJO"
    flaconete = "FLACONETE"
    frasco = "FRASCO"
    frasco_ampola = "FRASCO-AMPOLA"
    frasco_aplicador = "FRASCO-APLICADOR"
    frasco_transf = "FRASCO DE TRANSFERENCIA"
    frasco_got = "FRASCO GOTEJADOR"
    frasco_spray = "FRASCO SPRAY"
    lamina = "LÂMINA"
    pote = "POTE"
    seringa = "SERINGA PREENCHIDA"
    strip = "STRIP"
    tubo = "TUBO"
    caixa = "CAIXA"
    caixa_termica = "CAIXA TÉRMICA"
    cartucho = "CARTUCHO"
    aplicador = "APLICADOR"
    ativador = "ATIVADOR"
    bobeador = "BOMBEADOR"
    caneta = "CANETA APLICADORA"
    diluente = "DILUENTE"

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


if __name__ == '__main__':
    print(Tarja.vermelha.value)
