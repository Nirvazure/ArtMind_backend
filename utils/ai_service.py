class AnalyseAPI(Resource):

    def post(self):
        params = request.values
        if request.files:
            craft = request.files['imgfile']
            imgUrl = save_file(craft)
            if imgUrl:
                model = request.files['model_name']
                styleInfo = model.style()
                eraInfo = model.era()
                painterInfo = model.painter()
                data = {
                    'style': styleInfo,
                    'era': eraInfo,
                    'painter': painterInfo
                }
                return responseTo(data=data)
            return {msg: '文件类型错误'}, 400
        return {msg: '文件未上传'}, 400
