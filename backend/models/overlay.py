from bson import ObjectId
from datetime import datetime
from config.database import db

class Overlay:
    def __init__(self):
        self.collection = db.get_collection('overlays')
    
    def create(self, overlay_data):
        overlay_data['created_at'] = datetime.utcnow()
        overlay_data['updated_at'] = datetime.utcnow()
        result = self.collection.insert_one(overlay_data)
        return str(result.inserted_id)
    
    def get_all(self):
        overlays = list(self.collection.find())
        for overlay in overlays:
            overlay['_id'] = str(overlay['_id'])
        return overlays
    
    def get_by_id(self, overlay_id):
        overlay = self.collection.find_one({'_id': ObjectId(overlay_id)})
        if overlay:
            overlay['_id'] = str(overlay['_id'])
        return overlay
    
    def update(self, overlay_id, update_data):
        update_data['updated_at'] = datetime.utcnow()
        result = self.collection.update_one(
            {'_id': ObjectId(overlay_id)},
            {'$set': update_data}
        )
        return result.modified_count > 0
    
    def delete(self, overlay_id):
        result = self.collection.delete_one({'_id': ObjectId(overlay_id)})
        return result.deleted_count > 0