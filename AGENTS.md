# StackTracker - SaaS Architecture Decision Engine

## Project Overview
- **Project Name**: StackTracker
- **Type**: Single Page Application (SPA)
- **Core Functionality**: A question-oriented wizard that helps users define their business software idea by asking structured questions, then generating architecture recommendations, stack choices, module checklists, and CRUD matrices.
- **Target Users**: Entrepreneurs, developers, and teams planning to build SaaS products who need guidance on technology choices.

## UI/UX Specification

### Layout Structure
- **Header**: Logo/title, progress indicator
- **Main Content**: Question cards with answer options
- **Sidebar**: Supporting data panel (contextual knowledge)
- **Footer**: Navigation (Back/Next), Generate button when complete

### Visual Design
- **Color Palette**:
  - Primary: `#1e3a5f` (deep navy)
  - Secondary: `#2d5a87` (steel blue)
  - Accent: `#00d4aa` (teal/mint)
  - Background: `#0a1628` (dark navy)
  - Surface: `#12243d` (card background)
  - Text Primary: `#e8f1f8`
  - Text Secondary: `#8ba3bc`
- **Typography**:
  - Headings: "Outfit", sans-serif (600-700 weight)
  - Body: "DM Sans", sans-serif (400-500 weight)
  - Monospace: "JetBrains Mono" (for code/technical terms)
- **Spacing**: 8px base unit (8, 16, 24, 32, 48)
- **Visual Effects**:
  - Subtle gradient backgrounds
  - Card hover lift effect (transform: translateY(-2px))
  - Smooth transitions (0.3s ease)
  - Progress bar with glow effect
  - Answer options with radio/checkbox styling

### Components
1. **ProgressBar**: Shows completion percentage
2. **QuestionCard**: Current question with answer options
3. **KnowledgePanel**: Collapsible sidebar with supporting data
4. **AnswerOption**: Selectable cards for answers
5. **Navigation**: Back/Next buttons
6. **ResultsView**: Generated outputs (tabs for different documents)
7. **DownloadButton**: Export results as markdown

## Functionality Specification

### Question Categories
1. **Product Type** (defines interaction patterns)
2. **Client Architecture** (defines frontend needs)
3. **Data Requirements** (defines infrastructure)
4. **Scale** (defines database strategy)
5. **Team** (defines complexity tolerance)
6. **Backend Needs** (defines modules)

### Decision Logic
- Each answer maps to specific architecture consequences
- Decision tree based on:
  - SEO requirements → SSR/SSG decisions
  - Interactivity needs → SPA vs traditional
  - User scale → database/infrastructure
  - Multiple clients → BFF pattern
  - Team size → modular complexity

### Output Generation
- `architecture.md`: Frontend/backend architecture recommendation
- `stack.md`: Technology stack (framework, database, deployment)
- `modules.md`: Required backend modules
- `crud-matrix.md`: Database entities and CRUD operations
- `deployment.md`: Vercel + Supabase deployment config

### User Flow
1. Welcome screen with project name input
2. Sequential question categories
3. Review answers
4. Generate recommendations
5. View/download outputs

## Acceptance Criteria
- [x] All question categories display correctly
- [x] Supporting data shows for each question
- [x] Progress updates as user advances
- [x] Decision engine produces correct recommendations
- [x] All output documents generate with proper formatting
- [ ] Responsive design works on desktop/tablet
- [x] Smooth animations and transitions

## Implementation Progress

### Completed Features ✅
- 29+ questions with context-aware logic (mobile → iOS/Android, desktop → Win/Mac/Linux)
- Knowledge schema with all tech stack variables from transcript
- Module auto-generation based on product type + features
- Architecture recommendation engine with decision trees
- Enhanced output generation (Architecture, Stack, Checklist, Deployment)
- Ideas sidebar with save/load to localStorage
- Resume functionality - pick up where left off
- Progress tracking in idea list
- Complete Early button
- Reset current idea
- Delete selected ideas with checkboxes

### Remaining Features ⏳
- CRUD Matrix generator tab
- Enhanced deployment guide
- Responsive mobile/tablet design
- File export/download

## GitHub Issues
See https://github.com/puvuglobal/Stack-Tracker/issues
