import pandas as pd
from flask import Response

def convert_to_csv(data, file_title):
    df = pd.DataFrame(data)
    print(df)
    return Response(df.to_csv(index=False, encoding="UTF-8"), 
                    mimetype="text/csv", 
                    headers={"Content-Disposition": f"attachment; filename={file_title}"})