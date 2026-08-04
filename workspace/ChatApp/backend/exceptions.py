from fastapi.responses import JSONResponse


def server_error(message):

    return JSONResponse(

        status_code=500,

        content={

            "success": False,

            "message": message,

        },

    )
