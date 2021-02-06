from enum import Enum


class Tarja(Enum):
    choice = 'Escolha uma Tarja'
    sem_tarja = 'Sem Tarja'.upper()
    vermelha = 'Vermelha'.upper()
    vermelharest = 'Vermelha sob restrição'.upper()
    preta = 'Preta'.upper()

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class FormaFarmaceutica(Enum):
    choice = ('Escolha Forma Farmaceutica', "")
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
    nenhum = "Escolha a Classe Terapeutica"
    A02A = 'Antiácidos'.upper()
    A02D = 'Antiflatulentes'.upper()
    A02X = "outros antiacidos event medicamentos para ulcera event da  " \
           "flatulencia".upper()
    Analgesico = 'Analgésicos'.upper()
    Anestesico = 'Anestésicos'.upper()
    Anorexigeno = 'Anorexigenos'.upper()
    Ansiolitico = 'Ansiolíticos'.upper()
    a_hemor = 'Anti-hemorrágicos'.upper()
    a_hiperten = 'Anti-hipertensivos'.upper()
    a_histam = 'Anti-histamínicos'.upper()
    a_infne = 'Anti-inflamatórios não esteróides'.upper()
    a_agreg = 'Antiagregantes'.upper()
    a_anemic = 'Antianemicos'.upper()
    a_arritm = 'Antiarritmicos'.upper()
    a_asmat = 'Antiasmáticos'.upper()
    a_biotic = 'Antibióticos'.upper()
    a_coagul = 'Anticoagulantes'.upper()
    a_colica = 'Anticólica'.upper()
    a_concep = 'Anticoncepcionais'.upper()
    a_convul = 'Anticonvulsivantes'.upper()
    a_depres = 'Antidepressivos'.upper()
    a_diabet = 'Antidiabéticos'.upper()
    A03A = "antiespasmodicos event anticolinérgicos sintéticos".upper()
    A03C = "antiespasmodicos em associação com psicolépticos".upper()
    A03D = "antiespasmodicos em associação com analgésicos".upper()
    A03B = "Beladona event derivados simples".upper()
    A03F = "Propulsivos".upper()
    A07 = 'Antidiarreicos'.upper()
    A07A = 'Antiinfeciosos intestinais'.upper()
    A07C = 'elactrólitos com hidratos de carbono'.upper()
    A07D = 'antiprupulsivos'.upper()
    A07E = 'antiinflamatórios instestinais'.upper()
    A07F = 'microorganismos antidiarréicos'.upper()
    A08 = 'Preparados antiobesidade, excluindo dietéticos'.upper()
    A04 = 'Antieméticos event Antinauseantes'.upper()
    A05A = 'Terapêutica Biliar'.upper()
    A05B = 'Terapêutica hepática lipotrópicos'.upper()
    A05C = 'Medicamentos para Terapêutica biliar event hepática  ' \
           'associados'.upper()
    A10A = "Insulinas".upper()
    a_fungic = 'Antifúngicos'.upper()
    a_grips = 'Antigripais'.upper()
    a_inftop = 'Anti-inflamatorio Topico'.upper()
    a_lipem = 'Antilipemicos'.upper()
    a_lipemrc = 'Antilipemicos - Redutores do colesterol'.upper()
    a_mico = 'Antimicoticos'.upper().upper()
    a_micos = 'Antimicoticos Sistemicos'.upper()
    a_micot = 'Antimicoticos Topicos'.upper()
    a_paras = 'Antiparasitários'.upper()
    a_park = 'Antiparkinsonianos'.upper()
    a_piret = 'Antipiréticos'.upper()
    a_psic = 'Antipsicóticos'.upper()
    a_sept_or = 'Antissepticos Orais'.upper()
    a_termic = 'Antitérmicos'.upper()
    a_tuss = 'Antitussígenos'.upper()
    a_ulcer = 'Antiulcerosos'.upper()
    a_varic = 'Antivaricosos'.upper()
    a_vertig = 'Antivertiginosos'.upper()
    A11B = "Multivitaminas, associação".upper()
    A11C = "Multivitaminas, simples".upper()
    A13 = "Tonicos".upper()
    a_virais = 'Antivirais'.upper()
    ativador = 'Ativadores do Metabolismo Cerebral'.upper()
    benzod = 'Benzodiazepinas'.upper()
    betab = 'Betabloqueadores'.upper()
    bifosf = 'Bifosfonatos'.upper()
    broncod = 'Broncodilatadores'.upper()
    cardiot = 'Cardiotônicos'.upper()
    cicatriz = 'Cicatrizantes'.upper()
    coenzim = 'Coenzimas'.upper()
    cortic = 'Corticóides'.upper()
    cortic_s = 'Corticosteroides Sistemicos'.upper()
    cortic_t = 'Corticosteroides Topicos'.upper()
    Defatig = 'Defatigantes'.upper()
    descong = 'Descongestionantes nasais'.upper()
    diuret = 'Diuréticos'.upper()
    eletrol = 'Eletrolitos'.upper()
    A09 = 'Digestivos, incluindo Enzimas'.upper()
    pancreas = 'Pancreáticas'.upper()
    A15 = 'Estimulantes do Apetite'.upper()
    A16 = 'outros produtos para as vias digestivas event metabolismo'.upper()
    estimul_r = 'Estimulantes respiratórios'.upper()
    expect = 'Expectorantes'.upper()
    fitot = 'Fitoterápicos'.upper()
    sangue = 'Frações do sangue ou plasma exceto gamaglobulina'.upper()
    hepato = 'Hepatoprotetores'.upper()
    higien = 'Higiene'.upper()
    hipono = 'Hipnóticos'.upper()
    hipogli = 'Hipoglicemiantes Orais'.upper()
    homeop = 'Homeopáticos'.upper()
    hormon = 'Hormônios'.upper()
    imunomod = 'Imunomoduladores'.upper()
    imunosup = 'Imunossupressores'.upper()
    indutor = 'Indutores do Sono'.upper()
    A06 = 'Laxativos'.upper()
    manuart = 'Manutenção das articulações'.upper()
    mucol = 'Mucolíticos'.upper()
    neurole = 'Neurolepticos'.upper()
    plaquet = 'Plaquetarios'.upper()
    possos = 'Problemas ósseos'.upper()
    psico = 'Psicoanalépticos'.upper()
    relax = 'Relaxantes musculares'.upper()
    A14 = "anabolizantes".upper()
    repel = 'Repelentes'.upper()
    sedat = 'Sedativos'.upper()
    sedat_t = 'Sedativos da Tosse'.upper()
    soliso = 'Soluções Isomóticas Salinas Simples'.upper()
    vasocon = 'Vasoconstritores'.upper()
    vasod = 'Vasodilatadores'.upper()
    A11 = 'Vitaminas'.upper()
    A12A = 'Calcio'.upper()
    A12C = 'Outros suplementos minerais'.upper()

    @classmethod
    def list_names(cls):
        lista = [member.value for member in cls]
        return lista

    @classmethod
    def list_names_kivy(cls):
        lista = [{'text': member.value} for member in cls]
        return lista


class UnidadeDosagem(Enum):
    unidade = 'Escolha a unidade da dosagem'
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
    apresentacao = "Escolha a apresentação"
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
