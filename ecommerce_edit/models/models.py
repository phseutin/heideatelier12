from odoo import api, fields, models, _
import re

class Websitlocation(models.Model):
    _name = 'pickup.locations'
    _description = 'pickup locations desc'
    name=fields.Char('Pickup Locations')
    code=fields.Char('Location Code')

    date_ids = fields.One2many('pickup.dates', 'location_id','dates',store=True)
    
    #dates_format = fields.Text(string="Layout in Reports",
    #   help="Display format to use for addresses belonging to this country.\n\n"
    #       "You can use python-style string pattern with all the fields of the address "
    #         "(for example, use '%(street)s' to display the field 'street') plus"
    #         "\n%(state_name)s: the name of the state"
    #         "\n%(pickup_name)s: the code of the state"
    #         "\n%(pickup_locations)s: the name of the country"
    #         "\n%(country_code)s: the code of the country",
    #   default='%(street)s\n%(street2)s\n%(city)s %(pickup_name)s %(zip)s\n%(pickup_locations)s')

    #@api.multi
    #def get_dates_fields(self):
    #   self.ensure_one()
    #  return re.findall(r'\((.+?)\)', self.dates_format)


class Websitdates(models.Model):
    _name = 'pickup.dates'
    _description = 'pickup dates desc'
    name=fields.Char('Pickup Name')
    location_id = fields.Many2one('pickup.locations', 'location')



class ecommerce_edit(models.Model):
    _inherit = 'res.partner'
        
    location_id = fields.Many2one('pickup.locations', 'location')   
    date_id = fields.Many2one('pickup.dates', 'date')
    reseller_id = fields.Integer()
    





class ResLocations(models.Model):    
    _inherit = 'pickup.locations'

    def get_website_sale_locations(self, mode='billing'):
        return self.sudo().search([])

    def get_website_sale_dates(self, mode='billing'):
        return self.sudo().date_ids


class ecommers_saleorder(models.Model):
    _inherit='sale.order'

    x_location_id = fields.Many2one(related='partner_id.location_id',relation='pickup.locations' ,string='Kies hier je afhaalpunt',store=False,readonly=True)
    x_date_id = fields.Many2one(related='partner_id.date_id',relation='pickup.dates' ,string='Kies hier je afhaaldatum',store=False,readonly=True)
    x_reseller_id = fields.Integer(related='partner_id.reseller_id',string='Reseller',store=False,readonly=True)
    #x_reseller_name=fields.Char('Reseller',store=False,readonly=True)
    def _reseller(self):
        if self.x_reseller_id == 1:
            self.x_reseller_name='Chiro Heist Centrum'
        elif self.x_reseller_id == 2:
            self.x_reseller_name='Chiro Heist Statie'
        elif self.x_reseller_id == 3:
            self.x_reseller_name='Chiro Hallaar'
        elif self.x_reseller_id == 4:
            self.x_reseller_name='Chiro Putte'
        else :
            self.x_reseller_name='Chiro Grasheide'



    x_reseller_name= fields.Char(string='Reseller',store=False,compute='_reseller',readonly=True)
   ## x_reseller_name = fields.Selection([(1, 'Single'),(2, 'Married'),(3, 'Legal Cohabitant'),(4, 'Widower'),(5, 'Divorced')],string='Reseller',store=False,readonly=True)

   
                                               
    