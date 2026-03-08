# StackTracker - SaaS Architecture Decision Engine

A question-oriented wizard that helps entrepreneurs and developers define their business software idea. Answer questions about product type, clients, tech stack preferences, and get generated architecture blueprints with supportive context.

I really wanna just say that if we tackle this project as a community we can gift a opensource tool that'd help tons of young devs succeed in the wilderness of the corporate establishment. With new and exciting tools like agentic skills and swarms building has never been easier with the right people. Schema builds, security compliance and principle of system architecture is almost a after thought. Most builds today are insecure shipped productions that hit the marketplace where your 8 year old kid can purchase a silly banana treat from a game. Then your most intimate details are on the web, no rls, no backend sometimes, no real thought for stack design entirely. This wizard should help create a checklist, tree and schema to help keep young shippers intact with compliancy standards while they ship new and exciting things. As we develop this new and fun repo, planning your tech stack will become easier when shipping SaaS related productions. Please enjoy. If you have an idea or a comment....let me know I might be thinking it but haven't had the time to build this. It is open so, feel free to make a edit. Just don't delete anything. Be responsible. 

##  Features

### Question Wizard
- **29+ intelligent questions** covering product type, client architecture, frontend/backend, scale, deployment
- **Context-aware logic**: Selecting "mobile" reveals iOS/Android options; "desktop" reveals Windows/Mac/Linux
- **Tech stack implications** shown for each answer choice
- **Supporting knowledge panel** explaining why each choice matters

### Smart Decision Engine
- **Knowledge schema** with every variable from comprehensive tech stack research
- **Module auto-generation** based on product type + features (marketplace → orders, inventory, payments)
- **Architecture recommendations** using decision trees (SEO → SSR, high interactivity → SPA)
- **Scale-aware** suggestions (100 users vs 1M+ have different infrastructure needs)

### Ideas Management
- **Save multiple ideas** to localStorage
- **Resume where you left off** - picks up at last answered question
- **Progress tracking** shows completion status in sidebar
- **Delete multiple** ideas with checkbox selection

### Output Generation
- **Architecture Blueprint** - frontend, backend, database, architecture recommendations
- **Tech Stack** - framework, rendering strategy, state management, services
- **Implementation Checklist** - phase-by-phase task list with required modules
- **Deployment Guide** - step-by-step Vercel + Supabase setup

##  Quick Start

1. Open `index.html` in any modern browser
2. Enter your project name
3. Answer the questions (or click "Complete Early")
4. Generate your blueprint
5. View/download the architecture documents

##  How It Works

### Question Flow
1. **Product Type** → Defines core modules needed
2. **Client Architecture** → Mobile/Web/Desktop + platforms
3. **Frontend** → Framework, SEO, interactivity, state, styling
4. **Backend** → Platform, database, auth, realtime, payments, search
5. **Scale** → Infrastructure requirements
6. **Deployment** → Hosting, CDN
7. **Team** → Architecture complexity

### Decision Logic Example
```
Product: Marketplace
  → Modules: orders, inventory, payments, search, messaging

Client: Mobile + Desktop
  → BFF pattern recommended
  → PWA for mobile, Web for desktop

SEO: Yes
  → SSR required (Next.js)

Scale: 100K users
  → Read replicas recommended
  → Redis caching essential
```

##  What's Generated

### Architecture Blueprint
- Overview (frontend, backend, database, scale)
- Product analysis
- Client architecture details
- Architecture recommendations
- Complete tech stack summary

### Tech Stack Document
- Frontend: framework, rendering, state, styling
- Backend: platform, database, auth, realtime, search, payments
- Deployment: hosting, CDN, scale target

### Implementation Checklist
- Required modules (auto-generated)
- Phase 1: Foundation (setup, auth, DB)
- Phase 2: Core Features (product-specific)
- Phase 3: Polish (UX, performance)
- Phase 4: Launch (production)

### Deployment Guide
- Prerequisites
- Backend setup with SQL
- Frontend configuration
- Environment variables reference
- Production checklist

##  Tech Stack

- **Single HTML file** - No build step required
- **Vanilla JavaScript** - No frameworks
- **localStorage** - Persistent ideas storage
- **CSS Variables** - Easy theming
- **Google Fonts** - Outfit + DM Sans

##  Files

```
StackTracker/
├── index.html              # Main application
├── AGENTS.md              # Project specification
├── knowledge-schema.json  # Complete tech decision knowledge base
├── Data supporting repo.txt # Source transcript data
└── README.md              # This file
```

##  Customization

### Adding Questions
Edit the `questions` array in `index.html`:
```javascript
{ 
  id: 'unique_id', 
  category: 'Category Name', 
  title: 'Question title?', 
  desc: 'Description', 
  type: 'single' | 'multiple',
  condition: 'question_id', // optional - show only if answered
  conditionValue: ['value1', 'value2'], // optional
  options: [
    { v: 'value', t: 'Title', d: 'Description', i: 'emoji', stack: 'Tech stack' }
  ],
  know: 'Supporting knowledge panel text'
}
```

### Extending Knowledge Schema
Edit `knowledgeSchema` in `index.html`:
```javascript
const knowledgeSchema = {
  productTypes: {
    mytype: { modules: ['module1', 'module2'] }
  },
  // ... more categories
};
```

##  To Do

- [ ] CRUD Matrix generator tab
- [ ] Enhanced deployment guide
- [ ] Responsive mobile/tablet design
- [ ] File export/download feature

##  License

MIT

##  Contributing

Issues and PRs welcome at https://github.com/puvuglobal/Stack-Tracker
