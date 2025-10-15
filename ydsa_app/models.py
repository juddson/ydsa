from datetime import datetime
from .extensions import db

class Subscriber(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    wants_newsletter = db.Column(db.Boolean, default=False, nullable=False)
    # for future compliance / list hygiene
    consent_ts = db.Column(db.DateTime, nullable=True)
    unsubscribed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    source = db.Column(db.String(64), nullable=True)  # e.g., "website"

    def __repr__(self):
        return f"<Subscriber {self.email}>"
