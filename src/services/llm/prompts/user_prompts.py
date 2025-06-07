def query_and_services(query: str, services: str | dict):
    return (
        f"{query}.\n Los servicios disponibles para obtener informacion son:\n{services}"
    )


def query_and_data(query: str, data: str | dict):
    return f"{query}.\n Usa los siguientes datos para responder mi query:\n{data}"
