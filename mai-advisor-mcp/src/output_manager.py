"""
Output Manager for MAI Advisor - Handles file-based workflow for MCP and HF Space.

Workflow:
1. MCP tool call/user input --> topic/location
2. Orchestrator makes 3 API calls for Bing, DuckDuckGo, Google dorks
3. Orchestrator informs expert advisors of topic/focus
4. Experts generate strategic plans (max 2700 tokens) --> advisors_output/{expert-name}.{datetime}.md
5. Orchestrator reviews all plans --> orchestrator_output/grant-plan-and-overview.{datetime}.md

Directory Structure:
- advisors_output/ - Individual expert strategic plans (markdown, max 2700 tokens)
- orchestrator_output/ - Final enterprise-grade grant plan and overview (markdown)
- grant_dorks/ - Search dorks for Bing, DuckDuckGo, Google
"""
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class OutputManager:
    """
    Manages file-based output workflow for MAI Advisor.
    
    Workflow:
    1. Expert advisors write strategic plans (markdown) to advisors_output/
    2. Orchestrator reads all expert strategic plans
    3. Orchestrator generates enterprise-grade grant plan (markdown) to orchestrator_output/
    
    File naming:
    - Advisors: {expert-name}.{YYYYMMDD_HHMMSS}.md
    - Orchestrator: grant-plan-and-overview.{YYYYMMDD_HHMMSS}.md
    - Dorks: dorks.{YYYYMMDD_HHMMSS}.json
    """
    
    def __init__(self, base_dir: Optional[str] = None):
        """
        Initialize output manager.
        
        Args:
            base_dir: Base directory for outputs (defaults to project root)
        """
        if base_dir is None:
            # Default to project root
            base_dir = Path(__file__).parent.parent
        
        self.base_dir = Path(base_dir)
        
        # Create directory structure
        self.advisors_dir = self.base_dir / "advisors_output"
        self.orchestrator_dir = self.base_dir / "orchestrator_output"
        self.dorks_dir = self.base_dir / "grant_dorks"
        self.agent_instructions_dir = self.base_dir / "agent-instructions"
        
        # Create directories
        self.advisors_dir.mkdir(parents=True, exist_ok=True)
        self.orchestrator_dir.mkdir(parents=True, exist_ok=True)
        self.dorks_dir.mkdir(parents=True, exist_ok=True)
        self.agent_instructions_dir.mkdir(parents=True, exist_ok=True)
    
    def save_expert_plan(self, expert_name: str, content: str, topic: str = "") -> str:
        """
        Save expert strategic plan as markdown.
        
        Args:
            expert_name: Name of expert (financial, grant, research, etc.)
            content: Markdown content (max 2700 tokens recommended)
            topic: Optional topic for metadata
            
        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{expert_name}.{timestamp}.md"
        filepath = self.advisors_dir / filename
        
        # Write markdown file
        filepath.write_text(content, encoding='utf-8')
        
        return str(filepath)
    
    def save_orchestrator_plan(self, content: str, topic: str = "") -> str:
        """
        Save orchestrator's final enterprise-grade grant plan as markdown.
        
        Args:
            content: Markdown content of comprehensive grant plan
            topic: Optional topic for metadata
            
        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"grant-plan-and-overview.{timestamp}.md"
        filepath = self.orchestrator_dir / filename
        
        # Write markdown file
        filepath.write_text(content, encoding='utf-8')
        
        return str(filepath)
    
    def save_ai_agent_todo(self, content: str) -> str:
        """
        Save AI agent todo/instruction file as markdown to dedicated agent-instructions folder.
        
        Args:
            content: Markdown content with AI agent instructions
            
        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"agent-todo.{timestamp}.md"
        filepath = self.agent_instructions_dir / filename
        
        # Write markdown file
        filepath.write_text(content, encoding='utf-8')
        
        return str(filepath)
    
    def read_expert_plans(self, topic: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Read all expert strategic plans.
        
        Args:
            topic: Optional filter by topic (searches in content)
            
        Returns:
            List of dicts with {"expert": name, "filepath": path, "content": markdown}
        """
        plans = []
        
        for filepath in sorted(self.advisors_dir.glob("*.md"), reverse=True):
            content = filepath.read_text(encoding='utf-8')
            
            # Extract expert name from filename (before first dot)
            expert_name = filepath.stem.split('.')[0]
            
            # Filter by topic if specified
            if topic and topic.lower() not in content.lower():
                continue
            
            plans.append({
                "expert": expert_name,
                "filepath": str(filepath),
                "filename": filepath.name,
                "content": content,
                "timestamp": filepath.stat().st_mtime
            })
        
        return plans
    
    def read_orchestrator_plans(self, topic: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Read all orchestrator grant plans.
        
        Args:
            topic: Optional filter by topic (searches in content)
            
        Returns:
            List of dicts with {"filepath": path, "content": markdown}
        """
        plans = []
        
        for filepath in sorted(self.orchestrator_dir.glob("*.md"), reverse=True):
            content = filepath.read_text(encoding='utf-8')
            
            # Filter by topic if specified
            if topic and topic.lower() not in content.lower():
                continue
            
            plans.append({
                "filepath": str(filepath),
                "filename": filepath.name,
                "content": content,
                "timestamp": filepath.stat().st_mtime
            })
        
        return plans
    
    def save_dorks(self, topic: str, location: Optional[str], dorks: Dict[str, str]) -> str:
        """
        Save generated dorks to file.
        
        Args:
            topic: Grant search topic
            location: Optional location
            dorks: Dict of search engine dorks
            
        Returns:
            Path to saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = self._sanitize_filename(topic)
        
        filename = f"{timestamp}_dorks_{safe_topic}.json"
        filepath = self.dorks_dir / filename
        
        data = {
            "generated_at": datetime.now().isoformat(),
            "topic": topic,
            "location": location or "Not specified",
            "dorks": dorks
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return str(filepath)
    
    def list_expert_files(self) -> List[Dict[str, Any]]:
        """
        List all expert strategic plan files with metadata.
        
        Returns:
            List of file metadata dicts
        """
        files = []
        
        for filepath in sorted(self.advisors_dir.glob("*.md"), reverse=True):
            stat = filepath.stat()
            expert_name = filepath.stem.split('.')[0]
            files.append({
                "path": str(filepath),
                "filename": filepath.name,
                "expert": expert_name,
                "size_kb": round(stat.st_size / 1024, 2),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "type": "expert_plan"
            })
        
        return files
    
    def list_orchestrator_files(self) -> List[Dict[str, Any]]:
        """
        List all orchestrator grant plan files with metadata.
        
        Returns:
            List of file metadata dicts
        """
        files = []
        
        for filepath in sorted(self.orchestrator_dir.glob("*.md"), reverse=True):
            stat = filepath.stat()
            files.append({
                "path": str(filepath),
                "filename": filepath.name,
                "size_kb": round(stat.st_size / 1024, 2),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "type": "grant_plan"
            })
        
        return files
    
    def get_session_outputs(self, topic: str) -> Dict[str, Any]:
        """
        Get all outputs related to a specific topic/session.
        
        Args:
            topic: Topic to search for
            
        Returns:
            Dict with expert plans and orchestrator plans
        """
        expert_plans = self.read_expert_plans(topic=topic)
        orchestrator_plans = self.read_orchestrator_plans(topic=topic)
        
        return {
            "topic": topic,
            "expert_plans": expert_plans,
            "orchestrator_plans": orchestrator_plans,
            "total_experts": len(expert_plans),
            "total_plans": len(orchestrator_plans)
        }
    
    def _sanitize_filename(self, text: str, max_length: int = 50) -> str:
        """
        Sanitize text for use in filename.
        
        Args:
            text: Text to sanitize
            max_length: Maximum length
            
        Returns:
            Sanitized filename-safe string
        """
        # Replace problematic characters
        safe = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in text)
        # Replace spaces with underscores
        safe = safe.replace(' ', '_')
        # Limit length
        safe = safe[:max_length]
        # Remove trailing underscores
        safe = safe.rstrip('_')
        
        return safe.lower()
    
    def cleanup_old_files(self, days: int = 30) -> Dict[str, int]:
        """
        Remove files older than specified days.
        
        Args:
            days: Age threshold in days
            
        Returns:
            Dict with counts of removed files
        """
        from datetime import timedelta
        
        threshold = datetime.now() - timedelta(days=days)
        removed = {
            "advisors": 0,
            "orchestrator": 0,
            "dorks": 0
        }
        
        for directory, key in [
            (self.advisors_dir, "advisors"),
            (self.orchestrator_dir, "orchestrator"),
            (self.dorks_dir, "dorks")
        ]:
            for filepath in directory.glob("*.json"):
                stat = filepath.stat()
                modified = datetime.fromtimestamp(stat.st_mtime)
                
                if modified < threshold:
                    filepath.unlink()
                    removed[key] += 1
        
        return removed


# Global output manager instance
output_manager = OutputManager()
