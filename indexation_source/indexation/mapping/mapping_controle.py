"""
  This is the module tests mapping_controle
  """


def corrige_date_oeie_avis(date):
    """
      This method replaces "/" with "-" and '-' with 'T'
      """
    if date == "1970/07/04":
        return None
    else:
        date = date.replace('/', '-')
        date = date.replace(' ', 'T')
        return date
