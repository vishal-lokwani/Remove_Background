from odoo import models, fields,api,http
from PIL import Image
from io import BytesIO
import base64
from rembg import remove  
import logging
import urllib.request
import os
from odoo.http import request,route
from werkzeug.utils import secure_filename
from odoo.exceptions import UserError




_logger = logging.getLogger(__name__)


class RemoveBgModel(models.Model):
    _name = 'remove_bg.model'
    _description = 'Remove background of an image'

    image = fields.Binary(string='Image')
    processed_image = fields.Binary(string='Processed Image', readonly=True)

    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)

    # @api.model
    # def create(self, vals):        
    #         record = super(RemoveBgModel, self).create(vals)
    #         return record
    

    @api.model
    def remove_background(self, record_ids):   
        _logger.info('It is running bro')     
        for record in self.env['remove_bg.model'].browse(record_ids):
            if record.image:                
                image_data = base64.b64decode(record.image)                
                output_image_data = remove(image_data)                
                record.processed_image = base64.b64encode(output_image_data)    
            else:
                raise UserError('You must upload an image before removing the background.')                                     

    def download_processed_image(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/image?model=remove_bg.model&id=%s&field=processed_image' % (self.id),
            # 'url': '/web/content/%s/%s/processed_image/download/%s' % (self._name, self.id, self.processed_image),
            'target': 'self',            
        }

                
    # @api.model
    # def action_open_bg_remove(self,records):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Custom Remove Background',
    #         'res_model': 'remove_bg.model',
    #         'view_mode': 'form',
    #         'view_id': self.env.ref('custom_bg_remove.view_image_background_removal_form').id,
    #         'target': 'current',
    #     }




# class RemoveBgModel(models.Model):
#     _name = 'remove_bg.model'
#     _description = 'Remove background from images'

#     name = fields.Char(string='Name', required=True)
#     image = fields.Binary(string='Image', attachment=True)
#     processed_image = fields.Binary(string='Processed Image', attachment=True)
#     processed_image_url = fields.Char(string='Processed Image URL')

#     @api.model
#     def remove_background(self, record_ids):
#         for record in self.env['remove_bg.model'].browse(record_ids):
#             if record.image:
#                 image_data = base64.b64decode(record.image)
#                 original_image = Image.open(BytesIO(image_data))
                
#                 # Remove the background
#                 processed_image = remove(original_image)
                
#                 # Save the processed image
#                 file_name = secure_filename('processed_image.png')
#                 processed_image_path = os.path.join(os.getcwd(), 'images', file_name)
#                 processed_image.save(processed_image_path)
                
#                 # Store the file path in the processed_image_url field
#                 processed_image_url = f'/images/{file_name}'
                
#                 # Encode the processed image to base64
#                 buffered = BytesIO()
#                 processed_image.save(buffered, format="PNG")
#                 processed_image_base64 = base64.b64encode(buffered.getvalue())
                
#                 # Update the record
#                 record.write({
#                     'processed_image_url': processed_image_url,
#                     'processed_image': processed_image_base64
#                 })
        
#         return super(RemoveBgModel, self).create(record_ids)


# # class RemoveBgController(http.Controller):
#     @http.route('/remove_bg/upload', type='http', auth='public', methods=['POST'], csrf=False)
#     def upload_image(self, **kwargs):
#         file = request.httprequest.files['file']
#         image_data = file.read()
#         image_base64 = base64.b64encode(image_data)
        
#         record = request.env['remove_bg.model'].sudo().create({
#             'name': file.filename,
#             'image': image_base64,
#         })
        
#         download_link = request.httprequest.host_url + record.processed_image_url
#         return request.make_response(
#             download_link,
#             [('Content-Type', 'text/plain')]
#         )

#     @http.route('/images/<filename>', type='http', auth='public', methods=['GET'], csrf=False)
#     def serve_image(self, filename, **kwargs):
#         image_path = os.path.join(os.getcwd(), 'images', filename)
#         if os.path.exists(image_path):
#             with open(image_path, 'rb') as image_file:
#                 image_data = image_file.read()
#                 return request.make_response(image_data, [('Content-Type', 'image/png')])
#         return request.not_found()
